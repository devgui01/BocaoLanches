from django.contrib import admin
from .models import MovimentacaoEstoque


@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ['id', 'ingrediente', 'tipo', 'quantidade', 'custo_total', 'usuario', 'created_at']
    list_filter = ['tipo', 'created_at', 'ingrediente']
    search_fields = ['ingrediente__nome', 'observacoes']
    readonly_fields = ['custo_total', 'created_at']
    
    fieldsets = (
        ('Movimentação', {
            'fields': ('ingrediente', 'tipo', 'quantidade')
        }),
        ('Custos', {
            'fields': ('custo_unitario', 'custo_total')
        }),
        ('Informações', {
            'fields': ('observacoes', 'usuario', 'created_at')
        }),
    )
