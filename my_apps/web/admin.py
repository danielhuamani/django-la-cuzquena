# coding=utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from singlemodeladmin import SingleModelAdmin
from .models import Configuracion, Home, HomeBanner, Nosotros, Valores, Servicios, NuestrosServicios, Vehiculos, Contacto, MovilizarEmpresa, VehiculoBanner, ContactoBanner


class ConfiguracionAdmin(SingleModelAdmin):
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


class ValoresInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Valores
    extra = 1


class NosotrosAdmin(SingleModelAdmin, SummernoteModelAdmin):
    inlines = [ValoresInline]


class NuestrosServiciosAdmin(SummernoteModelAdmin):
    pass


class ServiciosAdmin(SingleModelAdmin, SummernoteModelAdmin):
    pass


class VehiculosAdmin(SummernoteModelAdmin):
    pass


class VehiculoBannerAdmin(SingleModelAdmin):
    pass


class ContactoBannerAdmin(SingleModelAdmin):
    pass

admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Valores)
admin.site.register(NuestrosServicios, NuestrosServiciosAdmin)
admin.site.register(Vehiculos, VehiculosAdmin)
admin.site.register(VehiculoBanner, VehiculoBannerAdmin)
admin.site.register(ContactoBanner, ContactoBannerAdmin)
admin.site.register(Contacto)
admin.site.register(MovilizarEmpresa)
admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(Home, HomeAdmin)
