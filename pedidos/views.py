from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Pedido, ItemPedido
from core.models import Produto, Cliente


def carrinho(request):
    """Página do carrinho de compras"""
    return render(request, 'pedidos/carrinho.html')


@require_http_methods(["POST"])
@csrf_exempt
def adicionar_ao_carrinho(request):
    """Adiciona produto ao carrinho (via AJAX)"""
    try:
        data = json.loads(request.body)
        produto_id = data.get('produto_id')
        quantidade = int(data.get('quantidade', 1))
        
        produto = get_object_or_404(Produto, id=produto_id, disponivel=True)
        
        if not produto.disponivel_para_venda:
            return JsonResponse({'success': False, 'message': 'Produto indisponível'})
        
        # Usa sessão para armazenar carrinho
        carrinho = request.session.get('carrinho', {})
        
        if str(produto_id) in carrinho:
            carrinho[str(produto_id)]['quantidade'] += quantidade
        else:
            carrinho[str(produto_id)] = {
                'produto_id': produto_id,
                'nome': produto.nome,
                'preco': float(produto.preco),
                'quantidade': quantidade,
                'imagem': produto.imagem.url if produto.imagem else '',
            }
        
        request.session['carrinho'] = carrinho
        request.session.modified = True
        
        return JsonResponse({
            'success': True,
            'message': 'Produto adicionado ao carrinho',
            'carrinho': carrinho
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


@require_http_methods(["POST"])
@csrf_exempt
def remover_do_carrinho(request):
    """Remove produto do carrinho"""
    try:
        data = json.loads(request.body)
        produto_id = str(data.get('produto_id'))
        
        carrinho = request.session.get('carrinho', {})
        if produto_id in carrinho:
            del carrinho[produto_id]
            request.session['carrinho'] = carrinho
            request.session.modified = True
        
        return JsonResponse({'success': True, 'carrinho': carrinho})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


@require_http_methods(["GET"])
def obter_carrinho(request):
    """Retorna o carrinho atual"""
    carrinho = request.session.get('carrinho', {})
    total = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    return JsonResponse({
        'carrinho': carrinho,
        'total': total,
        'quantidade_itens': sum(item['quantidade'] for item in carrinho.values())
    })


@require_http_methods(["POST"])
@csrf_exempt
def criar_pedido(request):
    """Cria um novo pedido"""
    try:
        data = json.loads(request.body)
        carrinho = request.session.get('carrinho', {})
        
        if not carrinho:
            return JsonResponse({'success': False, 'message': 'Carrinho vazio'})
        
        # Criar ou buscar cliente
        cliente = None
        nome_cliente = data.get('nome_cliente', '')
        telefone = data.get('telefone', '')
        instagram = data.get('instagram', '')
        
        if telefone:
            cliente, created = Cliente.objects.get_or_create(
                telefone=telefone,
                defaults={'nome': nome_cliente, 'instagram': instagram}
            )
        
        # Criar pedido
        pedido = Pedido.objects.create(
            cliente=cliente,
            nome_cliente=nome_cliente or 'Cliente',
            telefone=telefone,
            instagram=instagram,
            endereco_entrega=data.get('endereco_entrega', ''),
            observacoes=data.get('observacoes', ''),
            forma_pagamento=data.get('forma_pagamento', ''),
            status='pendente'
        )
        
        # Criar itens do pedido
        subtotal = 0
        for item_data in carrinho.values():
            produto = Produto.objects.get(id=item_data['produto_id'])
            item = ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=item_data['quantidade'],
                preco_unitario=produto.preco,
            )
            subtotal += item.subtotal
        
        pedido.subtotal = subtotal
        pedido.taxa_entrega = float(data.get('taxa_entrega', 0))
        pedido.desconto = float(data.get('desconto', 0))
        pedido.calcular_total()
        pedido.save()
        
        # Limpar carrinho
        request.session['carrinho'] = {}
        request.session.modified = True
        
        return JsonResponse({
            'success': True,
            'pedido_id': pedido.id,
            'total': float(pedido.total),
            'message': 'Pedido criado com sucesso!'
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


def checkout(request):
    """Página de checkout"""
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        messages.warning(request, 'Seu carrinho está vazio!')
        return redirect('core:cardapio')
    
    subtotal = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    return render(request, 'pedidos/checkout.html', {
        'subtotal': subtotal
    })


@login_required
def lista_pedidos(request):
    """Lista de pedidos para o admin"""
    pedidos = Pedido.objects.all().order_by('-created_at')
    return render(request, 'pedidos/lista_pedidos.html', {
        'pedidos': pedidos
    })


@login_required
def detalhe_pedido(request, pedido_id):
    """Detalhes de um pedido"""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/detalhe_pedido.html', {
        'pedido': pedido
    })
