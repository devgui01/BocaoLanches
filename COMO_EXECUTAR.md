# 🚀 Como Executar o Projeto Bocão Lanches

## Passo a Passo Completo

### 1️⃣ Abrir o Terminal/PowerShell

Abra o PowerShell ou Prompt de Comando na pasta do projeto:
```powershell
cd C:\Users\Administrador\BocaoLanches
```

### 2️⃣ Criar Ambiente Virtual (Recomendado)

```powershell
python -m venv venv
```

### 3️⃣ Ativar o Ambiente Virtual

**No Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Se der erro de política de execução, use:**
```powershell
.\venv\Scripts\activate
```

**Ou no CMD:**
```cmd
venv\Scripts\activate.bat
```

### 4️⃣ Instalar Dependências

```powershell
pip install -r requirements.txt
```

### 5️⃣ Criar Arquivo .env

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
SECRET_KEY=django-insecure-change-this-em-producao-12345
DEBUG=True
MERCADOPAGO_ACCESS_TOKEN=
INSTAGRAM_ACCESS_TOKEN=
```

### 6️⃣ Executar Migrações do Banco de Dados

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Criar Superusuário (Admin)

```powershell
python manage.py createsuperuser
```

Você será solicitado a informar:
- Username (nome de usuário)
- Email (opcional)
- Password (senha - não aparecerá na tela)
- Confirmar password

### 8️⃣ Executar o Servidor

```powershell
python manage.py runserver
```

Você verá uma mensagem como:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 9️⃣ Acessar o Sistema

Abra seu navegador e acesse:

- **Site Principal**: http://127.0.0.1:8000
- **Painel Admin**: http://127.0.0.1:8000/admin
- **Dashboard**: http://127.0.0.1:8000/dashboard/ (requer login)

### 🔟 Configurar Dados Iniciais

1. Acesse o Admin: http://127.0.0.1:8000/admin
2. Faça login com o superusuário criado
3. Configure:
   - **Categorias** (Core > Categorias)
   - **Ingredientes** (Core > Ingredientes)
   - **Produtos** (Core > Produtos)

---

## ⚡ Comandos Rápidos (Resumo)

```powershell
# 1. Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Criar .env (copie o conteúdo acima)

# 4. Migrar banco de dados
python manage.py makemigrations
python manage.py migrate

# 5. Criar admin
python manage.py createsuperuser

# 6. Executar servidor
python manage.py runserver
```

---

## 🛠️ Solução de Problemas Comuns

### Erro: "python não é reconhecido"
- Instale o Python: https://www.python.org/downloads/
- Marque a opção "Add Python to PATH" durante a instalação

### Erro ao ativar ambiente virtual
- No PowerShell, execute primeiro:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro: "ModuleNotFoundError: No module named 'django'"
- Certifique-se de que o ambiente virtual está ativado
- Execute: `pip install -r requirements.txt`

### Erro: "django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty"
- Crie o arquivo `.env` na raiz do projeto
- Adicione a linha: `SECRET_KEY=django-insecure-change-this-12345`

### Erro ao executar migrações
- Certifique-se de estar na pasta do projeto
- Verifique se o arquivo `db.sqlite3` não está bloqueado

### Porta 8000 já está em uso
- Use outra porta:
```powershell
python manage.py runserver 8001
```

---

## 📝 Próximos Passos Após Executar

1. ✅ Acesse o Admin e configure categorias
2. ✅ Cadastre ingredientes com estoque inicial
3. ✅ Crie produtos e associe ingredientes
4. ✅ Teste fazendo um pedido como cliente
5. ✅ Visualize o dashboard com estatísticas

---

## 🎯 Dica Extra

Você também pode usar o script de setup automático:

```powershell
python setup.py
```

Este script faz a maior parte da configuração automaticamente!
