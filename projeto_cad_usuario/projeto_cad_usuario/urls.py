from django.urls import path
from app_cad_usuario import views

urlpatterns = [
    # Rota, view responsavel, nome de referência
    path('',views.home, name='home'),
    path('usuarios/',views.usuarios, name='listagem_usuarios')
]
