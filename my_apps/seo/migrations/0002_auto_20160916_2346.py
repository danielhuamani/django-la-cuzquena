# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-17 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='meta_description',
            field=models.CharField(blank=True, help_text=b'M\xc3\xa1ximo 160 caracteres', max_length=160, verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='meta_title',
            field=models.CharField(blank=True, help_text=b'M\xc3\xa1ximo: 50 caracteres', max_length=50, verbose_name=b'T\xc3\xadtulo'),
        ),
    ]
