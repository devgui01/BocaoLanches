from django.contrib import admin
from .models import Categoria, Produto, Ingrediente, ProdutoIngrediente, Cliente


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativa', 'ordem']
    list_filter = ['ativa']
    search_fields = ['nome']


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'unidade_medida', 'quantidade_atual', 'quantidade_minima', 'estoque_baixo', 'ativo']
    list_filter = ['ativo', 'unidade_medida']
    search_fields = ['nome']
    readonly_fields = ['estoque_baixo']


class ProdutoIngredienteInline(admin.TabularInline):
    model = ProdutoIngrediente
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco', 'disponivel', 'disponivel_para_venda']
    list_filter = ['categoria', 'disponivel', 'estoque_controlado']
    search_fields = ['nome', 'descricao']
    inlines = [ProdutoIngredienteInline]
    readonly_fields = ['disponivel_para_venda']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'instagram']
    search_fields = ['nome', 'email', 'telefone', 'instagram']
