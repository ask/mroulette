from __future__ import absolute_import


def brand_unless_product_startswith(*s):

    def _match(product):
        return None if product.name.startswith(s) else product.brand
    return _match


SHORT_BRAND = {
    'Acon Digital': 'Acon',
    'Aegean Music': 'Aegean',
    'Audio Damage': 'AD',
    'Kush Audio': 'Kush',
    'Native Instruments': 'NI',
    'Slate Digital': 'Slate',
    'Tokyo Dawn Labs': 'TDR',
    'Goodhertz': 'GHz',
    'Abbey Road': brand_unless_product_startswith('EMI'),
    'MeldaProduction': None,
    'Softube': brand_unless_product_startswith(
        'Abbey Road', 'Mutronics', 'Summit Audio', 'Tonelux', 'Trident',
        'Tube-Tech', 'Valley People',
    ),
    'Solid State Logic': 'SSL',
}


def product_brand(product):
    brand = SHORT_BRAND.get(product.brand, product.brand)
    try:
        return brand(product)
    except TypeError:
        return brand


def product_and_brand(product):
    brand = product_brand(product)
    return ' '.join([brand, product.name]) if brand else product.name
