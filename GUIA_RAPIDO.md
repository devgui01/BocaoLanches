# Guia Rápido - Bocão Lanches

## 🚀 Início Rápido

### 1. Instalação

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Ou use o script de setup automático
python setup.py
```

### 2. Configuração Inicial

```bash
# Criar arquivo .env (copie do .env.example)
# Configure SECRET_KEY, DEBUG, etc.

# Executar migrações
python manage.py makemigrations
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver
```

### 3. Acessar o Sistema

- **Site Principal**: http://127.0.0.1:8000
- **Admin**: http://127.0.0.1:8000/admin
- **Dashboard**: http://127.0.0.1:8000/dashboard/ (requer login)

## 📋 Configuração dos Dados Iniciais

### Passo 1: Criar Categorias

1. Acesse o Admin: http://127.0.0.1:8000/admin
2. Vá em **Core > Categorias**
3. Clique em **Adicionar Categoria**
4. Exemplos:
   - Hambúrgueres
   - Bebidas
   - Acompanhamentos
   - Sobremesas

### Passo 2: Cadastrar Ingredientes

1. Vá em **Core > Ingredientes**
2. Adicione cada ingrediente:
   - Nome: Ex: "Carne Moída"
   - Unidade de Medida: kg, g, un, etc.
   - Quantidade Atual: Estoque inicial
   - Quantidade Mínima: Para alertas
   - Custo Unitário: Preço de compra

### Passo 3: Cadastrar Produtos

1. Vá em **Core > Produtos**
2. Adicione produtos:
   - Nome: Ex: "X-Burger"
   - Categoria: Selecione a categoria
   - Preço: Valor de venda
   - Imagem: Upload da foto (opcional)
   - Disponível: Marque se está à venda
   - Estoque Controlado: Marque se usa controle de ingredientes
3. Na aba "Ingredientes do Produtos", adicione os ingredientes necessários

## 🛒 Como Funciona para o Cliente

### Fluxo de Pedido

1. **Visualizar Cardápio**
   - Cliente acessa o site
   - Navega pelo cardápio
   - Vê produtos disponíveis

2. **Adicionar ao Carrinho**
   - Clica em "Adicionar" no produto
   - Produto vai para o carrinho
   - Pode ajustar quantidades

3. **Finalizar Pedido**
   - Vai ao carrinho
   - Clica em "Finalizar Pedido"
   - Preenche dados:
     - Nome completo
     - Telefone
     - Instagram (opcional)
     - Endereço de entrega
     - Forma de pagamento
   - Confirma o pedido

4. **Acompanhamento**
   - Pedido aparece na lista de pedidos (admin)
   - Status pode ser atualizado pelo admin

## 👨‍💼 Como Funciona para o Admin

### Dashboard

- Visualiza vendas do dia, semana e mês
- Vê lucro calculado automaticamente
- Gráficos de vendas
- Produtos mais vendidos
- Status dos pedidos

### Gestão de Pedidos

1. Acesse **Pedidos > Lista de Pedidos**
2. Veja todos os pedidos
3. Clique em "Ver" para detalhes
4. Atualize o status conforme necessário:
   - Pendente → Confirmado → Preparando → Pronto → Entregue

### Gestão de Estoque

1. Acesse **Estoque > Home**
2. Veja ingredientes e estoque atual
3. Alertas de estoque baixo aparecem automaticamente
4. Para registrar movimentação:
   - Selecione o ingrediente
   - Escolha o tipo (Entrada/Saída/Ajuste/Perda)
   - Informe quantidade e custo
   - Salve

### Histórico de Estoque

- Clique em "Histórico" em qualquer ingrediente
- Veja todas as movimentações
- Acompanhe custos e quantidades

## 💡 Dicas Importantes

### Controle de Estoque

- Quando um produto tem "Estoque Controlado" ativado, o sistema verifica automaticamente se há ingredientes suficientes
- Se não houver estoque, o produto aparece como "Indisponível"
- Registre sempre as entradas de ingredientes para cálculo correto de custos

### Cálculo de Lucro

- O lucro é calculado como: Vendas - Custos de Ingredientes
- Os custos são baseados nas movimentações de entrada de estoque
- Para cálculo preciso, registre sempre os custos ao comprar ingredientes

### Formas de Pagamento

- O sistema suporta: PIX, Dinheiro, Cartão de Crédito, Cartão de Débito, Mercado Pago
- Para integração real com Mercado Pago, configure o token no .env

### Instagram

- O campo Instagram é opcional
- Pode ser usado para identificar clientes
- Para integração completa, configure o token no .env

## 🔧 Solução de Problemas

### Erro ao executar migrações

```bash
# Limpe as migrações antigas (cuidado!)
python manage.py migrate --fake-initial
```

### Erro de CSRF

- Certifique-se de que o CSRF está habilitado
- Use {% csrf_token %} nos formulários

### Imagens não aparecem

- Verifique se a pasta `media/` existe
- Configure MEDIA_URL e MEDIA_ROOT no settings.py
- Em produção, configure servidor web para servir arquivos media

### Estoque não atualiza

- Verifique se está logado como admin
- Confirme que a movimentação foi salva corretamente
- Veja o histórico do ingrediente

## 📞 Suporte

Para dúvidas ou problemas:
- Instagram: @bocaolanches
- Verifique o README.md para mais informações
