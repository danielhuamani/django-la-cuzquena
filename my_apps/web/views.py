from django.shortcuts import render
from django.http import JsonResponse
from .models import HomeBanner, Home, Nosotros, Valores, Servicios, NuestrosServicios, Vehiculos, VehiculoBanner, ContactoBanner, Contacto, MovilizarEmpresa


def home(request):
    banners = HomeBanner.objects.all().order_by("posicion")
    home, create = Home.objects.get_or_create(pk=1)

    return render(request, "web/index.html", locals())


def nosotros(request):
    valores = Valores.objects.all().order_by("posicion")
    nosotros, create = Nosotros.objects.get_or_create(pk=1)
    HEAD = "NOSOTROS"
    return render(request, "web/nosotros.html", locals())


def servicios(request):
    nuestros_servicios = NuestrosServicios.objects.all().order_by("posicion")
    servicios, create = Servicios.objects.get_or_create(pk=1)
    HEAD = "SERVICIOS"
    return render(request, "web/servicios.html", locals())


def vehiculos(request):
    vehiculos = Vehiculos.objects.all().order_by("posicion")
    banner, create = VehiculoBanner.objects.get_or_create(pk=1)
    HEAD = "VEHICULOS"
    return render(request, "web/vehiculos.html", locals())


def contacto(request):
    banner, create = ContactoBanner.objects.get_or_create(pk=1)
    HEAD = "CONTACTO"
    return render(request, "web/contacto.html", locals())


def ajax_contacto(request):
    data = {'status': 'error'}
    if request.is_ajax():
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")
        mensaje = request.POST.get("mensaje")
        correo = request.POST.get("correo")
        contact = Contacto(nombre=nombre, telefono=telefono, correo=correo, mensaje=mensaje)
        contact.save()
        if contact:
            data['status'] = "ok"
    return JsonResponse(data)


def ajax_home(request):
    data = {'status': 'error'}
    if request.is_ajax():
        nombre = request.POST.get("nombre")
        mensaje = request.POST.get("mensaje")
        correo = request.POST.get("correo")
        contact = MovilizarEmpresa(nombre=nombre, correo=correo, mensaje=mensaje)
        contact.save()
        if contact:
            data['status'] = "ok"
    return JsonResponse(data)
