from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    
    path('lista_relatorio/', views.lista_relatorio, name='lista_relatorio'),
]
