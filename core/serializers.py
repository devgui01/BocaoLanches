from rest_framework import serializers
from .models import Produto, Categoria, Ingrediente, ProdutoIngrediente


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao', 'ordem']


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nome', 'unidade_medida']


class ProdutoIngredienteSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(read_only=True)
    
    class Meta:
        model = ProdutoIngrediente
        fields = ['ingrediente', 'quantidade']


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    ingredientes = ProdutoIngredienteSerializer(many=True, read_only=True)
    disponivel_para_venda = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'categoria', 'preco', 'imagem', 
                  'disponivel', 'disponivel_para_venda', 'ingredientes', 'created_at']
