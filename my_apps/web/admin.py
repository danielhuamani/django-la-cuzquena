# coding=utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from singlemodeladmin import SingleModelAdmin
from .models import Configuracion, Home, HomeBanner


class ConfiguracionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('telefono', 'correos', 'direccion', 'ciudad', 'mapa')
        }),
        ('Redes Sociales', {

            'fields': ('facebook', 'youtube', 'twitter'),
        }),
    )


class HomeAdmin(SingleModelAdmin, SummernoteModelAdmin):
    fieldsets = (
        ('Nosotros', {
            'fields': ('nosotros_image', 'nosotros')
        }),
        ('Servicios', {
            'fields': ('servicios_image', 'servicios')
        }),
        ('Vehículos', {
            'fields': ('vehiculos_image', 'vehiculos')
        }),

    )



class HomeBannerAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(HomeBanner, HomeBannerAdmin)
