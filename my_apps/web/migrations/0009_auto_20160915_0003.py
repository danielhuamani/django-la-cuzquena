# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 05:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_contactobanner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='Correo',
            new_name='correo',
        ),
    ]
