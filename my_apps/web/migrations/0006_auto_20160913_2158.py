# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20160913_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', filebrowser.fields.FileBrowseField(max_length=200, verbose_name='Vehiculo Banner')),
            ],
            options={
                'verbose_name': 'VehiculoBanner',
                'verbose_name_plural': 'VehiculoBanners',
            },
        ),
        migrations.AlterField(
            model_name='nosotros',
            name='image',
            field=filebrowser.fields.FileBrowseField(max_length=200, verbose_name='Nosotros Imagen'),
        ),
        migrations.AlterField(
            model_name='nuestrosservicios',
            name='imagen',
            field=filebrowser.fields.FileBrowseField(max_length=200, verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='vehiculos',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo_banner_vehiculo', to='web.VehiculoBanner'),
            preserve_default=False,
        ),
    ]
