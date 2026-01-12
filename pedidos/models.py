from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from core.models import Produto, Cliente


class Pedido(models.Model):
    """Pedidos realizados pelos clientes"""
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto'),
        ('saiu_entrega', 'Saiu para Entrega'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    FORMA_PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('pix', 'PIX'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('mercado_pago', 'Mercado Pago'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='pedidos', null=True, blank=True)
    nome_cliente = models.CharField(max_length=200, help_text="Nome do cliente (se não cadastrado)")
    telefone = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES, blank=True)
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxa_entrega = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    endereco_entrega = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    
    pagamento_id = models.CharField(max_length=200, blank=True, help_text="ID do pagamento no gateway")
    pagamento_status = models.CharField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"Pedido #{self.id} - {self.nome_cliente} - R$ {self.total}"

    def calcular_total(self):
        """Calcula o total do pedido"""
        self.total = self.subtotal + self.taxa_entrega - self.desconto
        return self.total

    def save(self, *args, **kwargs):
        if not self.total:
            self.calcular_total()
        super().save(*args, **kwargs)


class ItemPedido(models.Model):
    """Itens de um pedido"""
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='pedidos')
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens dos Pedidos'

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade} - R$ {self.subtotal}"

    def calcular_subtotal(self):
        """Calcula o subtotal do item"""
        self.subtotal = self.preco_unitario * self.quantidade
        return self.subtotal

    def save(self, *args, **kwargs):
        if not self.subtotal:
            self.calcular_subtotal()
        super().save(*args, **kwargs)
