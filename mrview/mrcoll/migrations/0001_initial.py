# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=8, verbose_name='type', choices=[(b'kontakt', b'kontakt'), (b'aumf', b'aumf'), (b'aufx', b'aufx'), (b'UVI', b'UVI'), (b'live', b'live'), (b'logic', b'logic'), (b'aumu', b'aumu'), (b'reaktor', b'reaktor')])),
                ('manufacturer', models.CharField(max_length=8, verbose_name='manufacturer')),
                ('subtype', models.CharField(max_length=8, verbose_name='subtype')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'audiounit',
                'verbose_name_plural': 'audiounits',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'ordering': ('brand', 'name'),
                'verbose_name': 'products',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mrcoll.Product')),
            ],
            options={
                'verbose_name': 'effects',
            },
            bases=('mrcoll.product',),
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mrcoll.Product')),
            ],
            options={
                'verbose_name': 'instrument',
                'verbose_name_plural': 'instruments',
            },
            bases=('mrcoll.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='au',
            field=models.ForeignKey(related_name='product', to='mrcoll.AudioUnit'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(related_name='products', to='mrcoll.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='mrcoll.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='audiounit',
            unique_together=set([('type', 'manufacturer', 'subtype')]),
        ),
    ]
