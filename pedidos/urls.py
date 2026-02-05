from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('carrinho/', views.carrinho, name='carrinho'),
    path('adicionar/', views.adicionar_ao_carrinho, name='adicionar_carrinho'),
    path('remover/', views.remover_do_carrinho, name='remover_carrinho'),
    path('obter/', views.obter_carrinho, name='obter_carrinho'),
    path('checkout/', views.checkout, name='checkout'),
    path('criar/', views.criar_pedido, name='criar_pedido'),
    path('lista/', views.lista_pedidos, name='lista_pedidos'),
    path('<int:pedido_id>/', views.detalhe_pedido, name='detalhe_pedido'),
]
