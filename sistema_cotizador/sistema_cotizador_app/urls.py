# url de la aplicacion creado para importar las urls al proyecto

from django.urls import path

# importamos las vistas creadas en views.py
from sistema_cotizador_app import views

# declaro las urls indicando las funciones de las views dentro de Sistema_cotizador_app
urlpatterns = [
    path('', views.inicio, name="inicio"),  # inicio no tendra url
    path('cotizaciones', views.cotizaciones, name="cotizaciones"),
    path('clientes', views.clientes, name="clientes"),
    path('vendedores', views.vendedores, name="vendedores"),
    path('serviciosproductos', views.serviciosproductos, name="serviciosproductos"),
    path('login', views.login, name="login"),
]
