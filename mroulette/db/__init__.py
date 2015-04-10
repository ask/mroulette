from __future__ import absolute_import

from collections import defaultdict

from .collection import Collection
from .effects import FX
from .instruments import INST

__all__ = ['FX', 'INST', 'fx_by_tag', 'fx_by_brand',
           'inst_by_tag', 'inst_by_brand']

fx_by_tag = defaultdict(set)
fx_by_brand = defaultdict(set)
inst_by_tag = defaultdict(set)
inst_by_brand = defaultdict(set)

for f in FX:
    fx_by_brand[f.brand].add(f)
    for tag in f.tags:
        fx_by_tag[tag.lower()].add(f)
for i in INST:
    inst_by_brand[i.brand].add(i)
    for tag in i.tags:
        inst_by_tag[tag.lower()].add(i)

effects = Collection(FX)
instruments = Collection(INST)
