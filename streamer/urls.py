from django.contrib import admin
from django.urls import path, include
from videos import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'relatorios' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include('videos.urls', namespace='relatorios'),), 
    path('', views.index, name='index'),
    path('listas/', views.lista_aula, name='lista_aula'),
    path('Relatorios/', views.lista_relatorio, name='lista_relatorio'),
    path('login/', views.user_login, name='user_login'),
    path('pagina_sucesso/', views.pagina_sucesso, name='pagina_sucesso'),
    path('pesquisar_por_nome/', views.pesquisar_por_nome, name='pesquisar_por_nome'),
    path('salvar_status_aula/<int:aula_id>/', views.salvar_status_aula, name='salvar_status_aula'),
    path('sair/', views.sair, name='sair'),
    path('home/', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('pesquisar_relatorio_por_nome/', views.pesquisar_relatorio_por_nome, name='pesquisar_relatorio_por_nome'),
    path('salvar_status_relatorio/<int:relatorio_id>/', views.salvar_status_relatorio, name='salvar_status_relatorio'),
    path('noticias/', views.lista_noticias, name='lista_noticias'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)