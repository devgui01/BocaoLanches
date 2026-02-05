# 🚀 Passo a Passo - Criar Serviço Web no Render

## 📍 Onde você está agora:
- ✅ Projeto "bocão-lanches" criado
- ✅ Ambiente "Produção" criado
- ⏭️ **PRÓXIMO**: Criar o serviço web

## 🎯 O que fazer AGORA:

### 1. Clique no botão: **"+ Criar novo serviço"**

### 2. Escolha o tipo de serviço:
- Selecione: **"Web Service"** (Serviço Web)

### 3. Conecte seu repositório Git:
- **GitHub/GitLab/Bitbucket**: Conecte sua conta
- Selecione o repositório: `BocaoLanches` (ou o nome do seu repo)
- Branch: `main` (ou `master`)

### 4. Configure o serviço:

#### **Nome do Serviço:**
```
bocao-lanches-web
```
ou simplesmente:
```
bocao-lanches
```

#### **Região:**
Escolha a mais próxima (ex: **São Paulo** ou **US East**)

#### **Branch:**
```
main
```
(ou `master` se for o caso)

#### **Root Directory:**
```
(Deixe vazio - se o projeto está na raiz)
```

### 5. **Build & Deploy:**

#### **Environment:**
```
Python 3
```

#### **Build Command:**
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

#### **Start Command:**
```bash
gunicorn bocao_lanches.wsgi:application
```

### 6. **Plano:**
- Escolha: **Free** (para começar)
- Ou: **Starter** ($7/mês) para melhor performance

### 7. **Clique em "Create Web Service"**

## 🔧 Depois de criar o serviço:

### 1. Criar Banco de Dados PostgreSQL:

1. No dashboard, clique em **"+ Novo"** → **"PostgreSQL"**
2. Configure:
   - **Nome**: `bocao-lanches-db`
   - **Database**: `bocaolanches`
   - **User**: `bocaolanches`
   - **Plano**: `Free`
3. Clique em **"Create Database"**

### 2. Conectar Banco ao Serviço Web:

1. Vá no seu serviço web criado
2. Vá em **"Environment"** (Variáveis de Ambiente)
3. Clique em **"Link Database"**
4. Selecione o banco `bocao-lanches-db`
5. A variável `DATABASE_URL` será preenchida automaticamente

### 3. Configurar Variáveis de Ambiente:

No serviço web, vá em **"Environment"** e adicione:

```
SECRET_KEY=(gere uma chave - veja abaixo)
DEBUG=False
ALLOWED_HOSTS=bocao-lanches.onrender.com
RENDER=True
```

**Para gerar SECRET_KEY**, execute no terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Deploy:

1. Clique em **"Manual Deploy"** → **"Deploy latest commit"**
2. Aguarde o build (pode levar 5-10 minutos)
3. Acompanhe os logs para ver o progresso

### 5. Criar Superusuário:

Após o deploy:
1. No Render, vá no seu serviço web
2. Clique em **"Shell"**
3. Execute:
```bash
python manage.py createsuperuser
```
4. Siga as instruções para criar o usuário admin

## ✅ Pronto!

Acesse: `https://bocao-lanches.onrender.com`

---

## 🆘 Se algo der errado:

- **Erro no build**: Verifique os logs no Render
- **Erro 500**: Verifique se `SECRET_KEY` está configurada
- **Banco não conecta**: Verifique se linkou o banco ao serviço
- **Arquivos estáticos**: Verifique se `collectstatic` está no build command
