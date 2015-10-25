from __future__ import absolute_import

from functools import partial
from collections import namedtuple

AU_TYPES = {'aufx', 'aumf', 'aumu'}

AUid = namedtuple('AUid', ('type', 'manufacturer', 'subtype'))
aufx = partial(AUid, 'aufx')
aumf = partial(AUid, 'aumf')
aumu = partial(AUid, 'aumu')
kontakt = AUid('kontakt', '-NI', 'NiO5')    # aumu
reaktor = AUid('reaktor', '-NI-', 'NiR5')   # aumu
reaktorFX = AUid('reaktor', '-NI-', 'NiR6')            # aufx
logic = AUid('logic', 'x', 'x')
live = AUid('live', 'y', 'y')
livefx = AUid('live', 'yfx', 'yfx')
uvi = AUid('UVI', 'UVI ', 'UVIW')

product = namedtuple('product', ('brand', 'name', 'au', 'tags'))
