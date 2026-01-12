from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from pedidos.models import Pedido, ItemPedido
from estoque.models import MovimentacaoEstoque
from core.models import Produto


@login_required
def dashboard(request):
    """Dashboard principal com gráficos e estatísticas"""
    hoje = timezone.now().date()
    mes_atual = hoje.replace(day=1)
    semana_atual = hoje - timedelta(days=hoje.weekday())
    
    # Períodos
    hoje_pedidos = Pedido.objects.filter(created_at__date=hoje)
    semana_pedidos = Pedido.objects.filter(created_at__date__gte=semana_atual)
    mes_pedidos = Pedido.objects.filter(created_at__date__gte=mes_atual)
    
    # Vendas
    vendas_hoje = hoje_pedidos.aggregate(total=Sum('total'))['total'] or Decimal('0')
    vendas_semana = semana_pedidos.aggregate(total=Sum('total'))['total'] or Decimal('0')
    vendas_mes = mes_pedidos.aggregate(total=Sum('total'))['total'] or Decimal('0')
    
    # Quantidade de pedidos
    qtd_pedidos_hoje = hoje_pedidos.count()
    qtd_pedidos_semana = semana_pedidos.count()
    qtd_pedidos_mes = mes_pedidos.count()
    
    # Pedidos por status
    pedidos_pendentes = Pedido.objects.filter(status='pendente').count()
    pedidos_preparando = Pedido.objects.filter(status='preparando').count()
    pedidos_prontos = Pedido.objects.filter(status='pronto').count()
    
    # Produtos mais vendidos (últimos 30 dias)
    ultimos_30_dias = hoje - timedelta(days=30)
    produtos_vendidos = ItemPedido.objects.filter(
        pedido__created_at__date__gte=ultimos_30_dias
    ).values('produto__nome').annotate(
        quantidade=Sum('quantidade'),
        total_vendas=Sum('subtotal')
    ).order_by('-quantidade')[:10]
    
    # Vendas por dia (últimos 7 dias)
    vendas_por_dia = []
    for i in range(6, -1, -1):
        data = hoje - timedelta(days=i)
        vendas_dia = Pedido.objects.filter(
            created_at__date=data,
            status__in=['confirmado', 'preparando', 'pronto', 'entregue']
        ).aggregate(total=Sum('total'))['total'] or Decimal('0')
        vendas_por_dia.append({
            'data': data.strftime('%d/%m'),
            'total': float(vendas_dia)
        })
    
    # Cálculo de lucro (simplificado)
    # Lucro = Vendas - Custos de ingredientes
    custos_mes = MovimentacaoEstoque.objects.filter(
        tipo='entrada',
        created_at__date__gte=mes_atual
    ).aggregate(total=Sum('custo_total'))['total'] or Decimal('0')
    
    lucro_mes = vendas_mes - custos_mes
    
    # Vendas por forma de pagamento
    formas_pagamento = Pedido.objects.filter(
        created_at__date__gte=mes_atual
    ).values('forma_pagamento').annotate(
        total=Sum('total'),
        quantidade=Count('id')
    )
    
    context = {
        'vendas_hoje': vendas_hoje,
        'vendas_semana': vendas_semana,
        'vendas_mes': vendas_mes,
        'qtd_pedidos_hoje': qtd_pedidos_hoje,
        'qtd_pedidos_semana': qtd_pedidos_semana,
        'qtd_pedidos_mes': qtd_pedidos_mes,
        'pedidos_pendentes': pedidos_pendentes,
        'pedidos_preparando': pedidos_preparando,
        'pedidos_prontos': pedidos_prontos,
        'produtos_vendidos': produtos_vendidos,
        'vendas_por_dia': vendas_por_dia,
        'lucro_mes': lucro_mes,
        'custos_mes': custos_mes,
        'formas_pagamento': formas_pagamento,
    }
    
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def relatorios(request):
    """Página de relatórios detalhados"""
    return render(request, 'dashboard/relatorios.html')
