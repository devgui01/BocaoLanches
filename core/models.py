from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class Categoria(models.Model):
    """Categorias de produtos (Hambúrgueres, Bebidas, Acompanhamentos, etc.)"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativa = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', 'nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    """Produtos disponíveis para venda"""
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    estoque_controlado = models.BooleanField(default=False, help_text="Se ativo, verifica estoque de ingredientes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['categoria', 'nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"

    @property
    def disponivel_para_venda(self):
        """Verifica se o produto está disponível considerando estoque"""
        if not self.disponivel:
            return False
        if self.estoque_controlado:
            # Verifica se todos os ingredientes têm estoque suficiente
            for item in self.ingredientes.all():
                if item.ingrediente.quantidade_atual < item.quantidade:
                    return False
        return True


class Ingrediente(models.Model):
    """Ingredientes utilizados nos produtos"""
    nome = models.CharField(max_length=200, unique=True)
    unidade_medida = models.CharField(
        max_length=50,
        choices=[
            ('kg', 'Quilograma'),
            ('g', 'Grama'),
            ('l', 'Litro'),
            ('ml', 'Mililitro'),
            ('un', 'Unidade'),
            ('cx', 'Caixa'),
            ('pac', 'Pacote'),
        ],
        default='un'
    )
    quantidade_atual = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    quantidade_minima = models.DecimalField(max_digits=10, decimal_places=3, default=0, 
                                           help_text="Quantidade mínima para alerta de estoque")
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return f"{self.nome} ({self.quantidade_atual} {self.unidade_medida})"

    @property
    def estoque_baixo(self):
        """Verifica se o estoque está abaixo do mínimo"""
        return self.quantidade_atual <= self.quantidade_minima


class ProdutoIngrediente(models.Model):
    """Relação entre produtos e ingredientes (receita)"""
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='ingredientes')
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name='produtos')
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(Decimal('0.001'))])

    class Meta:
        unique_together = ['produto', 'ingrediente']
        verbose_name = 'Ingrediente do Produto'
        verbose_name_plural = 'Ingredientes dos Produtos'

    def __str__(self):
        return f"{self.produto.nome} - {self.ingrediente.nome} ({self.quantidade})"


class Cliente(models.Model):
    """Clientes do sistema"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    instagram = models.CharField(max_length=100, blank=True, help_text="Usuário do Instagram")
    endereco = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
