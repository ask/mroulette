from __future__ import absolute_import


def find_info(p, key, sep=':'):
    return [t.split(sep) for t in p.tags if t.startswith(key + sep)]


def hp(p, cat=''):
    if 'logic' in p.tags:
        tag, menu = find_info(p, 'logic')[0]
        cat = '({0}:{1})'.format(tag, menu.capitalize())
    return '{0.name} ({0.brand}) {cat}'.format(p, cat=cat)


def header(s, fill='='):
    return '\n'.join([fill * len(s), s, fill * len(s)])
