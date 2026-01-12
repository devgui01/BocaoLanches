from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.filter(ativa=True)
    serializer_class = CategoriaSerializer


class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Produto.objects.filter(disponivel=True)
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'disponivel']
    search_fields = ['nome', 'descricao']
    ordering_fields = ['nome', 'preco', 'created_at']
    ordering = ['categoria', 'nome']

    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        """Retorna apenas produtos disponíveis para venda"""
        produtos = self.queryset.filter(disponivel=True)
        # Filtrar por disponibilidade de estoque
        produtos_disponiveis = [p for p in produtos if p.disponivel_para_venda]
        serializer = self.get_serializer(produtos_disponiveis, many=True)
        return Response(serializer.data)
