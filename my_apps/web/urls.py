# coding=utf-8
from django.conf.urls import url
from .views import home, nosotros, servicios, vehiculos, contacto

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^nosotros/$', nosotros, name="nosotros"),
    url(r'^servicios/$', servicios, name="servicios"),
    url(r'^vehiculos/$', vehiculos, name="vehiculos"),
    url(r'^contacto/$', contacto, name="contacto"),
]
