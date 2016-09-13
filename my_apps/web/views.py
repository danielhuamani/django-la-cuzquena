from django.shortcuts import render
from .models import HomeBanner, Home, Nosotros, Valores, Servicios, NuestrosServicios


def home(request):
    banners = HomeBanner.objects.all().order_by("posicion")
    home, create = Home.objects.get_or_create(pk=1)

    return render(request, "web/index.html", locals())


def nosotros(request):
    valores = Valores.objects.all().order_by("posicion")
    nosotros, create = Nosotros.objects.get_or_create(pk=1)
    return render(request, "web/nosotros.html", locals())


def servicios(request):
    nuestros_servicios = NuestrosServicios.objects.all().order_by("posicion")
    servicios, create = Servicios.objects.get_or_create(pk=1)
    return render(request, "web/servicios.html", locals())
