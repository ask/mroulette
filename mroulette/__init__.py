"""Musical roulette"""

from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(1, 0, 0, 'a2', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Ask Solem'
__contact__ = 'ask@celeryproject.org'
__homepage__ = 'http://twitter.com/asksol'
__docformat__ = 'restructuredtext'
__all__ = [
    'mroulette',
]

from mroulette import mroulette
