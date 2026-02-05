# Bocão Lanches - Sistema de Vendas e Gestão

Sistema completo de vendas e gestão para hamburgueria desenvolvido em Django.

## Funcionalidades

### Para Clientes
- ✅ Visualização do cardápio completo
- ✅ Carrinho de compras
- ✅ Sistema de pedidos online
- ✅ Checkout com múltiplas formas de pagamento
- ✅ Acompanhamento de pedidos

### Para Administrador
- ✅ Dashboard com gráficos de vendas e lucro
- ✅ Gestão completa de produtos e categorias
- ✅ Controle de estoque (entrada/saída de ingredientes)
- ✅ Gestão de pedidos (status, atualização)
- ✅ Relatórios de vendas
- ✅ Alertas de estoque baixo
- ✅ Histórico de movimentações

## Tecnologias Utilizadas

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Gráficos**: Chart.js
- **API REST**: Django REST Framework

## Instalação

### 1. Clone o repositório ou navegue até a pasta do projeto

```bash
cd BocaoLanches
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
MERCADOPAGO_ACCESS_TOKEN=seu-token-mercadopago
INSTAGRAM_ACCESS_TOKEN=seu-token-instagram
```

### 6. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 8. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

## Configuração Inicial

### 1. Acesse o Admin
- URL: http://127.0.0.1:8000/admin
- Faça login com o superusuário criado

### 2. Configure os Dados Básicos

#### Criar Categorias
- Vá em **Core > Categorias**
- Adicione categorias como: Hambúrgueres, Bebidas, Acompanhamentos, etc.

#### Cadastrar Ingredientes
- Vá em **Core > Ingredientes**
- Cadastre todos os ingredientes utilizados
- Defina unidade de medida, quantidade mínima e custo unitário

#### Cadastrar Produtos
- Vá em **Core > Produtos**
- Adicione produtos com nome, descrição, preço e imagem
- Associe os ingredientes necessários para cada produto

### 3. Configure o Instagram (Opcional)

Para integrar com Instagram, você precisará:
1. Criar uma aplicação no Facebook Developers
2. Obter o token de acesso do Instagram
3. Configurar no arquivo `.env`

## Estrutura do Projeto

```
BocaoLanches/
├── bocao_lanches/          # Configurações principais
│   ├── settings.py         # Configurações do Django
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # WSGI config
├── core/                   # App principal
│   ├── models.py          # Produtos, Categorias, Ingredientes, Clientes
│   ├── views.py           # Views principais
│   └── admin.py           # Admin personalizado
├── pedidos/               # App de pedidos
│   ├── models.py          # Pedidos e ItensPedido
│   └── views.py           # Views de pedidos
├── estoque/               # App de estoque
│   ├── models.py          # Movimentações de estoque
│   └── views.py           # Views de estoque
├── dashboard/             # App de dashboard
│   └── views.py           # Dashboard e relatórios
├── templates/             # Templates HTML
├── static/                # Arquivos estáticos (CSS, JS, imagens)
├── media/                 # Uploads de imagens
└── requirements.txt       # Dependências Python
```

## Uso do Sistema

### Cliente

1. **Visualizar Cardápio**: Acesse a página inicial ou menu "Cardápio"
2. **Adicionar ao Carrinho**: Clique em "Adicionar" nos produtos desejados
3. **Finalizar Pedido**: Vá ao carrinho e clique em "Finalizar Pedido"
4. **Preencher Dados**: Preencha nome, telefone, endereço e forma de pagamento
5. **Confirmar**: Clique em "Confirmar Pedido"

### Administrador

1. **Dashboard**: Visualize vendas, lucros e estatísticas
2. **Gestão de Pedidos**: Acompanhe e atualize status dos pedidos
3. **Estoque**: Registre entradas e saídas de ingredientes
4. **Produtos**: Gerencie produtos e categorias

## Integração com Pagamento

O sistema está preparado para integração com Mercado Pago. Para ativar:

1. Crie uma conta no Mercado Pago
2. Obtenha o Access Token
3. Configure no arquivo `.env`
4. Implemente a lógica de pagamento nas views (se necessário)

## Deploy em Produção

Para produção, recomenda-se:

1. Usar PostgreSQL ao invés de SQLite
2. Configurar `DEBUG=False`
3. Configurar `ALLOWED_HOSTS`
4. Usar servidor web (Nginx + Gunicorn)
5. Configurar arquivos estáticos e media
6. Usar HTTPS

## Suporte

Para dúvidas ou problemas, entre em contato através do Instagram: @bocaolanches

## Licença

Este projeto é de uso interno da Bocão Lanches.
