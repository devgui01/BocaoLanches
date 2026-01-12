from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.estoque_home, name='home'),
    path('movimentacao/', views.registrar_movimentacao, name='registrar_movimentacao'),
    path('historico/<int:ingrediente_id>/', views.historico_ingrediente, name='historico'),
]
