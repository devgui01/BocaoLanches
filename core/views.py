from django.shortcuts import render
from .models import Produto, Categoria


def index(request):
    """Página inicial"""
    categorias = Categoria.objects.filter(ativa=True)
    produtos_destaque = Produto.objects.filter(disponivel=True)[:6]
    return render(request, 'core/index.html', {
        'categorias': categorias,
        'produtos_destaque': produtos_destaque,
    })


def cardapio(request):
    """Página do cardápio completo"""
    categorias = Categoria.objects.filter(ativa=True).prefetch_related('produtos')
    return render(request, 'core/cardapio.html', {
        'categorias': categorias,
    })
