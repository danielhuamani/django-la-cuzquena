# coding=utf-8
from django.conf.urls import url
from .views import home, nosotros, servicios

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^nosotros/$', nosotros, name="nosotros"),
    url(r'^servicios/$', servicios, name="servicios"),
]
