# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from filebrowser.fields import FileBrowseField


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
    banner = FileBrowseField("Home Banner", max_length=200, directory='home_banner/',
        extensions=['.jpg', '.png', '.gif'])
    titulo = models.CharField("Titulo", max_length=60)
    subtitulo = models.CharField("Sub-Titulo", max_length=60)
    descripcion = models.TextField(u"Descripción")

    class Meta:
        verbose_name = "Home Banner"
        verbose_name_plural = "Home Banners"

    def __unicode__(self):
        return self.titulo


class Home(models.Model):
    nosotros = models.TextField(u"Descripción")
    nosotros_image = FileBrowseField("Nosostros Imagen", max_length=200, directory='nosotros/',
        extensions=['.jpg', '.png', '.gif'])
    servicios = models.TextField(u"Descripción")
    servicios_image = FileBrowseField("Servicios Imagen", max_length=200, directory='servicios/',
        extensions=['.jpg', '.png', '.gif'])
    vehiculos = models.TextField(u"Descripción")
    vehiculos_image = FileBrowseField("Vehiculos Imagen", max_length=200, directory='vehiculos/',
        extensions=['.jpg', '.png', '.gif'])

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"

    def __unicode__(self):
        return "Home Contenido"


class Nosotros(models.Model):
    banner = FileBrowseField("Nosotros Banner", max_length=200, directory='banner/',
        extensions=['.jpg', '.png', '.gif'])

    nosotros_amarillo = models.TextField(u"Nosotros texto amarillo")
    nosotros_plomo= models.TextField(u"Nosotros texto plomo")
    banner = FileBrowseField("Banner", max_length=200, directory='nosotros/',
        extensions=['.jpg', '.png', '.gif'])
    mision = models.TextField(u"Misión")
    vision = models.TextField(u"Visión")

    class Meta:
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotross"

    def __unicode__(self):
        return "Nosotros"


class Valores(models.Model):
    posicion = models.IntegerField(u"Posicion", default=0)
    nosotros = models.ForeignKey(Nosotros, related_name="nosotros_valores")
    imagen = FileBrowseField("Imagen", max_length=200, directory='valores/',
        extensions=['.jpg', '.png', '.gif'])
    titulo = models.CharField("Titulo", max_length=120)
    descripcion = models.TextField(u"Descripción")

    class Meta:
        verbose_name = "Valores"
        verbose_name_plural = "Valoress"

    def __unicode__(self):
        return u"%s" % (self.titulo)


class Servicios(models.Model):
    banner = FileBrowseField("Servicios Banner", max_length=200, directory='banner/',
        extensions=['.jpg', '.png', '.gif'])

    class Meta:
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotross"

    def __unicode__(self):
        return "Nosotros"


class NuestrosServicios(models.Model):
    posicion = models.IntegerField(u"Posicion", default=0)
    servicio = models.ForeignKey(Servicios, related_name="servicios_valores")
    imagen = FileBrowseField("Servicios", max_length=200, directory='servicios/',
        extensions=['.jpg', '.png', '.gif'])
    titulo = models.CharField("Titulo", max_length=120)
    descripcion = models.TextField(u"Descripción")

    class Meta:
        verbose_name = "Valores"
        verbose_name_plural = "Valoress"

    def __unicode__(self):
        return u"%s" % (self.titulo)


class Vehiculos(models.Model):
    posicion = models.IntegerField(u"Posicion", default=0)
    vehiculo = FileBrowseField("Vehiculos Imagen", max_length=200, directory='vehiculos/',
        extensions=['.jpg', '.png', '.gif'])
    descripcion = models.TextField(u"Descripción")

    class Meta:
        verbose_name = "Vehiculos"
        verbose_name_plural = "Vehiculoss"

    def __unicode__(self):
        return u"%s" % (self.posicion)


class Contacto(models.Model):
    nombre = models.CharField("Nombre", max_length=120)
    telefono = models.CharField("Telefono", max_length=20)
    Correo = models.EmailField("Correo")
    mensaje = models.TextField("Mensaje")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"

    def __unicode__(self):
        return u"%s" % (self.nombre)


class MovilizarEmpresa(models.Model):
    nombre = models.CharField("Nombre", max_length=120)
    Correo = models.EmailField("Correo")
    mensaje = models.TextField("Mensaje")

    class Meta:
        verbose_name = "Movilizar a tu Empresa"
        verbose_name_plural = "Movilizar a tu Empresas"

    def __unicode__(self):
        return u"%s" % (self.nombre)
