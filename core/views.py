from django.http import HttpResponse

def index(request):
    return HttpResponse("SITE NO AR - FUNCIONANDO")

def cardapio(request):
    return HttpResponse("CARDAPIO OK")
