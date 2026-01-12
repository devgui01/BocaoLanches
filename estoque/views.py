from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MovimentacaoEstoque
from core.models import Ingrediente


@login_required
def estoque_home(request):
    """Página principal de gestão de estoque"""
    ingredientes = Ingrediente.objects.filter(ativo=True)
    movimentacoes_recentes = MovimentacaoEstoque.objects.all()[:20]
    
    # Estatísticas
    ingredientes_estoque_baixo = [ing for ing in ingredientes if ing.estoque_baixo]
    
    return render(request, 'estoque/home.html', {
        'ingredientes': ingredientes,
        'movimentacoes_recentes': movimentacoes_recentes,
        'ingredientes_estoque_baixo': ingredientes_estoque_baixo,
    })


@login_required
@require_http_methods(["POST"])
@csrf_exempt
def registrar_movimentacao(request):
    """Registra uma nova movimentação de estoque"""
    try:
        data = json.loads(request.body)
        
        ingrediente_id = data.get('ingrediente_id')
        tipo = data.get('tipo')
        quantidade = float(data.get('quantidade', 0))
        custo_unitario = float(data.get('custo_unitario', 0))
        observacoes = data.get('observacoes', '')
        
        ingrediente = Ingrediente.objects.get(id=ingrediente_id)
        
        # Verificar se há estoque suficiente para saída
        if tipo in ['saida', 'perda'] and ingrediente.quantidade_atual < quantidade:
            return JsonResponse({
                'success': False,
                'message': f'Estoque insuficiente. Disponível: {ingrediente.quantidade_atual} {ingrediente.unidade_medida}'
            })
        
        movimentacao = MovimentacaoEstoque.objects.create(
            ingrediente=ingrediente,
            tipo=tipo,
            quantidade=quantidade,
            custo_unitario=custo_unitario,
            observacoes=observacoes,
            usuario=request.user
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Movimentação registrada com sucesso!',
            'movimentacao_id': movimentacao.id,
            'estoque_atual': float(ingrediente.quantidade_atual)
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


@login_required
def historico_ingrediente(request, ingrediente_id):
    """Histórico de movimentações de um ingrediente"""
    ingrediente = Ingrediente.objects.get(id=ingrediente_id)
    movimentacoes = MovimentacaoEstoque.objects.filter(ingrediente=ingrediente).order_by('-created_at')
    
    return render(request, 'estoque/historico.html', {
        'ingrediente': ingrediente,
        'movimentacoes': movimentacoes,
    })
