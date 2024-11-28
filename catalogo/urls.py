# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),  # Asegúrate de que esta línea esté presente
    path('filtrar/', views.filtrar, name='filtrar'),
    path('buscar/', views.buscar, name='buscar'),
    path('detalles/<int:id>/', views.detalles, name='detalles'),
    path('videojuego/<int:videojuego_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
]