# 🚀 Preparação Rápida para Deploy no Render

## ✅ Checklist Rápido

### 1. Verificar Arquivos Criados
Todos os arquivos necessários já foram criados:
- ✅ `render.yaml` - Configuração do Render
- ✅ `build.sh` - Script de build
- ✅ `requirements.txt` - Dependências atualizadas
- ✅ `runtime.txt` - Versão do Python
- ✅ `DEPLOY_RENDER.md` - Guia completo

### 2. Configurações Aplicadas
- ✅ Settings.py atualizado para produção
- ✅ WhiteNoise configurado para arquivos estáticos
- ✅ PostgreSQL configurado
- ✅ Segurança habilitada para produção
- ✅ Gunicorn adicionado ao requirements.txt

## 📝 Próximos Passos

### 1. Inicializar Git (se ainda não fez)
```bash
git init
git add .
git commit -m "Preparação para deploy no Render"
```

### 2. Criar Repositório no GitHub/GitLab
1. Crie um novo repositório no GitHub
2. Conecte seu projeto:
```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git branch -M main
git push -u origin main
```

### 3. Deploy no Render
Siga o guia completo em `DEPLOY_RENDER.md`

## 🔑 Variáveis de Ambiente Necessárias

No Render, configure estas variáveis:

```
SECRET_KEY=(gere uma chave segura)
DEBUG=False
ALLOWED_HOSTS=seu-app.onrender.com
RENDER=True
DATABASE_URL=(será preenchido ao linkar o banco)
```

## 🎯 Comandos Importantes

### Gerar SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Testar localmente com produção:
```bash
export DEBUG=False
export SECRET_KEY=sua-chave-aqui
python manage.py collectstatic
python manage.py migrate
gunicorn bocao_lanches.wsgi:application
```

## 📚 Documentação

- Guia completo: `DEPLOY_RENDER.md`
- Render Docs: https://render.com/docs

---

**Tudo pronto para deploy!** 🎉
