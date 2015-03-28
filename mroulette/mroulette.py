from __future__ import absolute_import
from __future__ import print_function, unicode_literals

import errno
import os
import sys
import random

from optparse import OptionParser, make_option as Option

from . import __version__
from .aupreset import aupreset
from .db import FX, INST, fx_by_tag, inst_by_tag, effects
from .exceptions import UnknownCommand
from .types import AU_TYPES
from .utils import hp, header

FMT = """\
{header}

reverb:    {reverb}
delay:     {delay}
special:   {special}
character: {character}
dynamics:  {dynamics}
eq:        {eq}
"""

OPTIONS = (
    Option('--logic', action='store_true',
           help='include Apple Logic Pro X effects/instruments'),
    Option('--live', action='store_true',
           help='include Ableton Live effects/instruments'),
)


def product_as_aupreset(product):
    if product.au.type not in AU_TYPES:
        raise NotImplementedError(
            'cannot make preset for type {0}'.format(product.au.type),
        )
    return aupreset(
        product.au.manufacturer,
        product.au.subtype,
        product.au.type,
        product.name,
    )


class mroulette(object):

    def __init__(self, stdout=sys.stdout, stderr=sys.stderr):
        self.stdout, self.stderr = stdout, stderr
        self.version = __version__
        self._seen_fx = set()
        self._tagdir_created = set()

        self.handlers = {
            'random': self.random,
            'list': self.list,
            'instruments': self.instruments,
            'effects': self.effects,
            'geninst': self.geninst,
            'genfx': self.genfx,
            'genfavinst': self.genfavinst,
            'genfavfx': self.genfavfx,
        }

    def random(self, logic=False, live=False):
        return FMT.format(
            header=header(hp(random.choice(list(INST)))),
            reverb=hp(self.uniq_fx_by_tag('reverb')),
            delay=hp(self.uniq_fx_by_tag('delay')),
            special=hp(self.uniq_fx_by_tag('special')),
            character=hp(self.uniq_fx_by_tag('character')),
            eq=hp(self.uniq_fx_by_tag('eq')),
            dynamics=hp(self.uniq_fx_by_tag('dynamics')),
        )

    def _list_db(self, collection, title):
        return '\n'.join([
            header(title),
            '\n'.join(sorted([' '.join(
                [i.brand, i.name]) for i in collection], key=unicode.lower,
            )),
        ])

    def instruments(self, live=False, logic=False):
        return self._list_db(INST, 'Instruments')

    def effects(self, live=False, logic=False):
        return self._list_db(FX, 'Effects')

    def list(self, live=False, logic=False):
        return '\n\n'.join([
            self.instruments(live, logic),
            self.effects(live, logic),
        ])

    def genfx(self, dest, live=False, logic=False):
        self.gen_presets(dest, fx_by_tag, live, logic)

    def geninst(self, dest, live=False, logic=False):
        self.gen_presets(dest, inst_by_tag, live, logic)

    def genfavfx(self, dest, ntags=1, live=False, logic=False):
        self.gen_favpresets(dest, FX, ntags, live, logic)

    def genfavinst(self, dest, ntags=1, live=False, logic=False):
        self.gen_brandpresets(dest, INST, live, logic)

    def mkdir_f(self, path):
        print('* creating dir %s' % (self.quote(path), ))
        try:
            os.mkdir(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass

    def quote(self, s, sep='"'):
        return ''.join([sep, s, sep])

    def gen_presets(self, dest, tags, live=False, logic=False):
        self.mkdir_f(dest)
        for tag, products in tags.iteritems():
            for product in products:
                self.save_preset_for_product(dest, product, tag)

    def save_preset_for_product(self, dest, product, tag, suffix='aupreset'):
        tagdir = os.path.join(dest, tag)
        try:
            preset = product_as_aupreset(product)
        except NotImplementedError:
            pass
        else:
            if tagdir not in self._tagdir_created:
                self.mkdir_f(tagdir)
                self._tagdir_created.add(tagdir)
            filename = os.path.join(
                tagdir, '.'.join([product.name, suffix]),
            )
            print('> preset for %s' % (self.quote(filename)), )
            with open(filename, 'w') as fh:
                try:
                    print(preset, file=fh)
                except NotImplementedError:
                    pass

    def gen_brandpresets(self, dest, collection,
                         live=False, logic=False):
        self.mkdir_f(dest)
        for product in collection:
            self.save_preset_for_product(dest, product, product.brand)

    def gen_favpresets(self, dest, collection,
                       ntags=1, live=False, logic=False):
        self.mkdir_f(dest)
        for product in collection:
            for tag in product.tags[:ntags]:
                self.save_preset_for_product(dest, product, tag)

    def uniq_fx_by_tag(self, tag):
        seen = self._seen_fx

        while 1:
            r = effects.random_by_tag(tag)
            if r not in seen:
                seen.add(r)
                return r

    def expanduser(self, value):
        if isinstance(value, basestring):
            return os.path.expanduser(value)
        return value

    def execute_from_commandline(self, argv=sys.argv):
        prog_name = os.path.basename(argv[0])
        options, args = OptionParser(
            prog=prog_name,
            usage=self.usage(),
            version=self.version,
            description=__doc__,
            option_list=OPTIONS,
        ).parse_args(argv[1:])
        options = {
            k: self.expanduser(v)
            for k, v in vars(options).items() if not k.startswith('_')
        }
        args = args if args else ['random']
        try:
            self.run(*args, **options)
        except UnknownCommand:
            self.execute_from_commandline([prog_name, '--help'])
            return os.EX_USAGE
        else:
            return os.EX_OK

    def run(self, command, *rest, **kwargs):
        try:
            handler = self.handlers[command]
        except KeyError:
            raise UnknownCommand(command)

        print(handler(*rest, **kwargs), file=self.stdout)

    def usage(self):
        return '%prog [options] [{0}]'.format(
            '|'.join(sorted(self.handlers.keys())),
        )
