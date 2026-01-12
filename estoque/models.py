from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from core.models import Ingrediente
from django.contrib.auth.models import User


class MovimentacaoEstoque(models.Model):
    """Movimentações de entrada e saída de estoque"""
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('ajuste', 'Ajuste'),
        ('perda', 'Perda'),
    ]

    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name='movimentacoes')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(Decimal('0.001'))])
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacoes = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentações de Estoque'

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.ingrediente.nome} - {self.quantidade}"

    def save(self, *args, **kwargs):
        """Atualiza o estoque do ingrediente ao salvar"""
        if not self.pk:  # Se é uma nova movimentação
            if self.tipo == 'entrada':
                self.ingrediente.quantidade_atual += self.quantidade
            elif self.tipo in ['saida', 'perda']:
                self.ingrediente.quantidade_atual -= self.quantidade
            elif self.tipo == 'ajuste':
                # Ajuste pode ser positivo ou negativo
                self.ingrediente.quantidade_atual += self.quantidade
            
            # Atualiza custo unitário se fornecido
            if self.custo_unitario > 0:
                self.custo_total = self.quantidade * self.custo_unitario
                # Atualiza custo médio do ingrediente
                if self.tipo == 'entrada':
                    # Cálculo de custo médio ponderado
                    estoque_anterior = self.ingrediente.quantidade_atual - self.quantidade
                    custo_anterior = estoque_anterior * self.ingrediente.custo_unitario
                    custo_novo = self.custo_total
                    quantidade_total = self.ingrediente.quantidade_atual
                    if quantidade_total > 0:
                        self.ingrediente.custo_unitario = (custo_anterior + custo_novo) / quantidade_total
            
            self.ingrediente.save()
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Reverte a movimentação ao deletar"""
        if self.tipo == 'entrada':
            self.ingrediente.quantidade_atual -= self.quantidade
        elif self.tipo in ['saida', 'perda']:
            self.ingrediente.quantidade_atual += self.quantidade
        elif self.tipo == 'ajuste':
            self.ingrediente.quantidade_atual -= self.quantidade
        
        self.ingrediente.save()
        super().delete(*args, **kwargs)
