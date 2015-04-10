from __future__ import absolute_import

import random

from collections import Counter, defaultdict


class Collection(object):

    def __init__(self, db):
        self.db = db
        self.by_tag = defaultdict(set)
        self.by_brand = defaultdict(set)
        self._rand_by_tag = None
        self._rand_by_brand = None
        self._most_common = None
        self.update_indices()

    def __iter__(self):
        return iter(self.db)

    def update_indices(self):
        self.by_tag.clear()
        self.by_brand.clear()

        for product in self.db:
            self.by_brand[product.brand].add(product)
            for tag in product.tags:
                self.by_tag[tag].add(product)
        self._rand_by_tag = defaultdict(list)
        self._rand_by_brand = self._prepare_randomness()
        for brand, products in self._rand_by_brand.iteritems():
            for product in products:
                for tag in product.tags:
                    self._rand_by_tag[tag.lower()].append(product)

    def _prepare_randomness(self):
        result = defaultdict(list)
        brands = self._most_common = Counter(p.brand for p in self)
        most_total = None
        for i, (brand, total) in enumerate(brands.most_common()):
            if i:
                diff = most_total - total
                products = list(self.by_brand[brand])
                result[brand].extend(products)
                result[brand].extend(
                    products[j % total]
                    for j in range(min(diff, max(total, 8)))
                )
                random.shuffle(result[brand])
            else:
                most_total = total
        return result

    def random_by_tag(self, tag):
        return random.choice(self._rand_by_tag[tag.lower()])
