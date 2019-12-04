from django.urls import path
from .views import home,proc,graf,ram,gab,eliminar_proce,modificar_proce, eliminar_graf, modificar_graf,eliminar_ram,modificar_ram,eliminar_gab,modificar_gab, listar_proce, listar_graf, listar_ram, listar_gab, registro_usuario
from . import views

urlpatterns = [
    path('', home, name = "home"),
    path('proc', proc, name = "proc"),
    path('graf', graf, name = "graf"),
    path('ram', ram, name = "ram"),
    path('gab', gab, name = "gab"),
    path('listar_proce/', listar_proce, name = "listar_proce"),
    path('listar_graf/', listar_graf, name = "listar_graf"),
    path('listar_ram/', listar_ram, name = "listar_ram"),
    path('listar_gab/', listar_gab, name = "listar_gab"),
    path('eliminar_proce/<id>/', eliminar_proce, name="eliminar_proce"),
    path('modificar_proce/<id>/', modificar_proce, name="modificar_proce"),
    path('eliminar_graf/<id>/', eliminar_graf, name="eliminar_graf"),
    path('modificar_graf/<id>/', modificar_graf, name="modificar_graf"),
    path('eliminar_ram/<id>/', eliminar_ram, name="eliminar_ram"),
    path('modificar_ram/<id>/', modificar_ram, name="modificar_ram"),
    path('eliminar_gab/<id>/', eliminar_gab, name="eliminar_gab"),
    path('modificar_gab/<id>/', modificar_gab, name="modificar_gab"), 
    path('registro/', registro_usuario, name='registro_usuario')
]

