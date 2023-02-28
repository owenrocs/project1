from django.urls import path
from . import views     # Importa las vistas de la aplicación del directorio actual

urlpatterns = [
    path('', views.index, name='index'),
    path('procesamiento', views.procesamiento, name='procesamiento')
]