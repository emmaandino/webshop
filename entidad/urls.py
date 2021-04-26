from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca", views.acerca_de, name="acerca"),
    path("cliente", views.clientes, name="cliente"),
    path("nuevocliente", views.cargar_cliente, name="nuevocliente"),
    path("editarcliente/(?P<pk>\d+)$", views.editar_cliente, name="editarcliente"),
    path("borrarcliente/(?P<pk>\d+)$", views.borrar_cliente, name="borrarcliente"),
    path("articulos", views.articulo, name="articulos"),
    path("categoria", views.categoria, name="categoria"),
    path("nuevacategoria", views.cargar_categoria, name="nuevacategoria"),
    path("editarcategoria", views.editar_categoria, name="editarcategoria"),
    path("borrarcategoria", views.borrar_categoria, name="borrarcategoria"),
    path("nuevoarticulo", views.cargar_articulo, name="nuevoarticulo"),
    path("editararticulo/(?P<pk>\d+)$", views.editar_articulo, name="editararticulo"),
    path("borrararticulo/(?P<pk>\d+)$", views.borrar_articulo, name="borrararticulo"),
    path("contacto", views.show_contact, name="contacto")
]
