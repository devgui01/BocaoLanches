from django.urls import path
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'produtos', api_views.ProdutoViewSet, basename='produto')
router.register(r'categorias', api_views.CategoriaViewSet, basename='categoria')

urlpatterns = router.urls
