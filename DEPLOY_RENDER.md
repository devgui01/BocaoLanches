# 🚀 Guia de Deploy no Render - Bocão Lanches

## 📋 Pré-requisitos

1. Conta no Render: https://render.com
2. Repositório Git (GitHub, GitLab ou Bitbucket)
3. Projeto commitado e enviado para o repositório

## 🔧 Passo a Passo

### 1. Preparar o Repositório Git

```bash
# Inicializar git (se ainda não tiver)
git init

# Adicionar arquivos
git add .

# Commit inicial
git commit -m "Preparação para deploy no Render"

# Conectar ao repositório remoto (GitHub/GitLab)
git remote add origin SEU_REPOSITORIO_URL
git push -u origin main
```

### 2. Criar Serviço Web no Render

1. Acesse: https://dashboard.render.com
2. Clique em **"New +"** → **"Web Service"**
3. Conecte seu repositório Git
4. Configure o serviço:

#### Configurações Básicas:
- **Name**: `bocao-lanches` (ou o nome que preferir)
- **Region**: Escolha a região mais próxima (ex: São Paulo)
- **Branch**: `main` (ou `master`)
- **Root Directory**: (deixe vazio se o projeto está na raiz)

#### Build & Deploy:
- **Environment**: `Python 3`
- **Build Command**: 
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- **Start Command**: 
  ```bash
  gunicorn bocao_lanches.wsgi:application
  ```

### 3. Criar Banco de Dados PostgreSQL

1. No dashboard do Render, clique em **"New +"** → **"PostgreSQL"**
2. Configure:
   - **Name**: `bocao-lanches-db`
   - **Database**: `bocaolanches`
   - **User**: `bocaolanches`
   - **Plan**: `Free` (ou pago se preferir)
3. Anote as credenciais de conexão

### 4. Configurar Variáveis de Ambiente

No serviço web criado, vá em **"Environment"** e adicione:

#### Variáveis Obrigatórias:
```
SECRET_KEY=sua-chave-secreta-super-segura-aqui
DEBUG=False
ALLOWED_HOSTS=seu-app.onrender.com
DATABASE_URL=(será preenchido automaticamente se conectar o banco)
RENDER=True
```

#### Variáveis Opcionais:
```
MERCADOPAGO_ACCESS_TOKEN=seu-token-mercadopago
INSTAGRAM_ACCESS_TOKEN=seu-token-instagram
```

#### Conectar Banco de Dados:
1. No serviço web, vá em **"Environment"**
2. Clique em **"Link Database"**
3. Selecione o banco criado
4. A variável `DATABASE_URL` será preenchida automaticamente

### 5. Deploy Automático

Após configurar tudo:
1. Clique em **"Manual Deploy"** → **"Deploy latest commit"**
2. Aguarde o build e deploy (pode levar alguns minutos)
3. Acesse sua URL: `https://seu-app.onrender.com`

## 🔐 Gerar SECRET_KEY Segura

Execute no terminal:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie o resultado e use como `SECRET_KEY` no Render.

## 📝 Primeiro Acesso

1. Acesse: `https://seu-app.onrender.com/admin`
2. Crie um superusuário:
   - No Render, vá em **"Shell"** do seu serviço web
   - Execute: `python manage.py createsuperuser`
   - Siga as instruções

## 🎨 Configurar Arquivos Estáticos

Os arquivos estáticos (CSS, JS, imagens) são servidos automaticamente pelo WhiteNoise após o `collectstatic`.

## 📸 Configurar Upload de Imagens

Para upload de imagens de produtos funcionar:

1. No Render, vá em **"Environment"**
2. Adicione variável:
   ```
   MEDIA_ROOT=/opt/render/project/src/media
   ```

Ou configure um serviço de storage (AWS S3, Cloudinary, etc.)

## 🔄 Deploy Contínuo

O Render faz deploy automático sempre que você fizer push para o repositório conectado.

## 🐛 Troubleshooting

### Erro 500 Internal Server Error
- Verifique os logs no Render Dashboard
- Confirme que `DEBUG=False` e `SECRET_KEY` está configurada
- Verifique se as migrações foram executadas

### Arquivos estáticos não aparecem
- Verifique se `collectstatic` está no build command
- Confirme que `STATIC_ROOT` está configurado
- Verifique se WhiteNoise está instalado

### Banco de dados não conecta
- Verifique se o banco está linkado ao serviço web
- Confirme que `DATABASE_URL` está preenchida
- Verifique se `psycopg2-binary` está no requirements.txt

### Migrações não executam
- Adicione `python manage.py migrate` no build command
- Ou execute manualmente via Shell do Render

## 📊 Monitoramento

- **Logs**: Acesse "Logs" no dashboard do Render
- **Métricas**: Veja uso de CPU, memória e rede
- **Health Checks**: Configure em "Health Check Path" (ex: `/`)

## 💰 Planos

- **Free**: Ideal para testes e desenvolvimento
- **Starter**: $7/mês - Melhor performance
- **Professional**: $25/mês - Recursos avançados

## 🔗 URLs Importantes

- Dashboard: https://dashboard.render.com
- Documentação: https://render.com/docs
- Status: https://status.render.com

## ✅ Checklist Final

- [ ] Repositório Git configurado
- [ ] Serviço Web criado no Render
- [ ] Banco PostgreSQL criado e linkado
- [ ] Variáveis de ambiente configuradas
- [ ] Build command configurado
- [ ] Start command configurado
- [ ] SECRET_KEY gerada e configurada
- [ ] DEBUG=False
- [ ] Superusuário criado
- [ ] Deploy realizado com sucesso
- [ ] Site acessível e funcionando

---

**Dica**: Mantenha um arquivo `.env.example` no repositório com todas as variáveis necessárias (sem valores sensíveis) para facilitar configuração.
