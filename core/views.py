from django.shortcuts import render


def index(request):
    context = {
        'produtos_destaque': []
    }
    return render(request, 'core/index.html', context)


def cardapio(request):
    context = {
        'categorias': []
    }
    return render(request, 'core/cardapio.html', context)
