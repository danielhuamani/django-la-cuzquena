# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from filer.fields.image import FilerImageField


class Configuracion(models.Model):
    telefono = models.CharField(u"Teléfono", max_length=120, help_text="Separar los telefonos mediante: |")
    correos = models.EmailField("Correo")
    direccion = models.CharField(u"Dirección", max_length=120)
    ciudad = models.CharField(u"Ciudad - Distrito", max_length=20)
    mapa = GeopositionField()
    youtube = models.URLField("Youtube", blank=True, null=True)
    facebook = models.URLField("facebook", blank=True, null=True)
    twitter = models.URLField("Twitter", blank=True, null=True)

    class Meta:
        verbose_name = "Configuracion"
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        pass


class HomeBanner(models.Model):
    banner = FilerImageField(null=True, blank=True, related_name="home_banner")
    titulo = models.CharField("Titulo", max_length=60)
    subtitulo = models.CharField("Sub-Titulo", max_length=60)
    descripcion = models.TextField(u"Descripción")

    class Meta:
        verbose_name = "Home Banner"
        verbose_name_plural = "Home Banners"

    def __unicode__(self):
        pass


class Home(models.Model):
    nosotros = models.TextField(u"Descripción")
    nosotros_image = FilerImageField(verbose_name='Imagen', related_name="nosotros_image")
    servicios = models.TextField(u"Descripción")
    servicios_image = FilerImageField(verbose_name='Imagen', related_name="servicios_image")
    vehiculos = models.TextField(u"Descripción")
    vehiculos_image = FilerImageField(verbose_name='Imagen', related_name="vehiculos_image")


    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"

    def __unicode__(self):
        return "Home Contenido"
