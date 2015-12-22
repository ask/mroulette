from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as __

from mroulette.types import AU_CHOICES


def import_all():
    from mroulette import db
    Effect.objects.import_from_collection(db.effects)
    Instrument.objects.import_from_collection(db.instruments)


class ProductManager(models.Manager):

    def import_from_collection(self, collection):
        for product in collection.db:
            self.import_from_product(product)

    def import_from_product(self, product):
        brand, _ = self.model.Brand.objects.get_or_create(name=product.brand)
        name = product.name
        au = self.model.AudioUnit.objects.import_from_AUid(product.au)
        p, created = self.get_or_create(
            brand=brand, name=name, defaults={'au': au},
        )
        if created:
            p.save()
            for tag in product.tags:
                tag, _ = self.model.Tag.objects.get_or_create(name=tag)
                p.tags.add(tag)
            p.save()


class AudioUnitManager(models.Manager):

    def import_from_AUid(self, auid):
        return self.get_or_create(
            type=auid.type,
            manufacturer=auid.manufacturer,
            subtype=auid.subtype,
        )[0]


class AudioUnit(models.Model):
    objects = AudioUnitManager()

    type = models.CharField(
        __('type'),
        choices=zip(AU_CHOICES, AU_CHOICES),
        blank=False,
        max_length=8,
    )
    manufacturer = models.CharField(
        __('manufacturer'),
        max_length=8,
        blank=False,
    )
    subtype = models.CharField(
        __('subtype'),
        max_length=8,
        blank=False,
    )
    created_at = models.DateTimeField(__('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(__('updated_at'), auto_now=True)

    class Meta:
        unique_together = ('type', 'manufacturer', 'subtype')
        verbose_name = __('audiounit')
        verbose_name_plural = __('audiounits')

    def __unicode__(self):
        return '{0.type} {0.manufacturer} {0.subtype}'.format(self)


class Brand(models.Model):
    name = models.CharField(__('name'), max_length=64, unique=True)
    created_at = models.DateTimeField(__('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(__('updated_at'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = __('brand')
        verbose_name_plural = __('brands')

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(__('name'), max_length=64, unique=True)
    created_at = models.DateTimeField(__('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(__('updated_at'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = __('tag')
        verbose_name_plural = __('tags')

    def __unicode__(self):
        return '{0.name}'.format(self)


class Product(models.Model):
    AudioUnit = AudioUnit
    Brand = Brand
    Tag = Tag

    abstract = True
    objects = ProductManager()

    name = models.CharField(__('name'), max_length=64)
    brand = models.ForeignKey(Brand, related_name='products')
    au = models.ForeignKey(AudioUnit, related_name='product')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(__('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(__('updated_at'), auto_now=True)

    class Meta:
        ordering = ('brand', 'name')
        verbose_name = __('product')
        verbose_name = __('products')

    def __unicode__(self):
        return '{0.brand.name} - {0.name}'.format(self)


class Instrument(Product):
    objects = ProductManager()

    class Meta:
        verbose_name = __('instrument')
        verbose_name_plural = __('instruments')


class Effect(Product):
    objects = ProductManager()

    class Meta:
        verbose_name = __('effect')
        verbose_name_plural = __('effects')
