from django.conf.urls import url, include
from django.contrib import admin

from .views import index, listar, consulta_listar, detalles_vista, tipos_pokemon

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^listar/$', consulta_listar, name='consultar_list'),
    url(r'^listar/(?P<cantidad>[0-9]+)/$', listar, name='resultado_lista'),
    url(r'^elemento/detalles/(?P<id>[0-9]+)$', detalles_vista, name='detalles'),
    url(r'^listar/tipo/(?P<id>[0-9]+)$', tipos_pokemon, name="tipos"),
]
