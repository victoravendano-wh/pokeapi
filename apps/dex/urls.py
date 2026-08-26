from django.conf.urls import url, include
from django.contrib import admin
#from .views import , detalles_vista, tipos_pokemon
from .views import index, listar, consulta_listar

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^listar/$', consulta_listar, name='consultar_list'),
    url(r'^listar/(?P<cantidad>[0-9]+)/$', listar, name='resultado_lista'),
]
