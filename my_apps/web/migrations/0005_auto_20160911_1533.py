# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-11 20:33
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20160911_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='servicios_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicios_image', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='home',
            name='vehiculos_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos_image', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='banner',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_banner', to='filer.Image'),
        ),
    ]
