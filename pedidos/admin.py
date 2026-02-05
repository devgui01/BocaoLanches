from django.contrib import admin
from .models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ['subtotal']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_cliente', 'status', 'total', 'forma_pagamento', 'created_at']
    list_filter = ['status', 'forma_pagamento', 'created_at']
    search_fields = ['nome_cliente', 'telefone', 'instagram']
    readonly_fields = ['subtotal', 'total', 'created_at', 'updated_at']
    inlines = [ItemPedidoInline]
    
    fieldsets = (
        ('Cliente', {
            'fields': ('cliente', 'nome_cliente', 'telefone', 'instagram')
        }),
        ('Pedido', {
            'fields': ('status', 'forma_pagamento', 'observacoes')
        }),
        ('Valores', {
            'fields': ('subtotal', 'taxa_entrega', 'desconto', 'total')
        }),
        ('Entrega', {
            'fields': ('endereco_entrega',)
        }),
        ('Pagamento', {
            'fields': ('pagamento_id', 'pagamento_status')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at')
        }),
    )
