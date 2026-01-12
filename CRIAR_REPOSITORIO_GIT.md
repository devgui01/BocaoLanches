# 📦 Criar Repositório Git para Bocão Lanches

## 🎯 Objetivo
Criar um repositório no GitHub e fazer upload do projeto para conectar ao Render.

## 📝 Passo a Passo

### 1. Inicializar Git Localmente

Execute no terminal (na pasta do projeto):

```powershell
cd C:\Users\Administrador\BocaoLanches
git init
git add .
git commit -m "Projeto inicial - Sistema Bocão Lanches"
```

### 2. Criar Repositório no GitHub

#### Opção A: Via Site do GitHub (Recomendado)

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `BocaoLanches` (ou `bocao-lanches`)
   - **Description**: `Sistema de vendas e gestão para hamburgueria`
   - **Visibility**: Escolha **Public** (gratuito) ou **Private**
   - **NÃO marque** "Initialize with README" (já temos arquivos)
3. Clique em **"Create repository"**

#### Opção B: Via GitHub CLI (se tiver instalado)

```bash
gh repo create BocaoLanches --public --source=. --remote=origin --push
```

### 3. Conectar Repositório Local ao GitHub

Após criar o repositório no GitHub, você receberá uma URL. Use uma destas:

**Se escolheu HTTPS:**
```powershell
git remote add origin https://github.com/SEU_USUARIO/BocaoLanches.git
```

**Se escolheu SSH:**
```powershell
git remote add origin git@github.com:SEU_USUARIO/BocaoLanches.git
```

### 4. Fazer Push dos Arquivos

```powershell
git branch -M main
git push -u origin main
```

Você será solicitado a fazer login no GitHub.

## 🔐 Autenticação no GitHub

### Opção 1: Personal Access Token (Recomendado)

1. Acesse: https://github.com/settings/tokens
2. Clique em **"Generate new token"** → **"Generate new token (classic)"**
3. Configure:
   - **Note**: `Render Deploy`
   - **Expiration**: Escolha um prazo
   - **Scopes**: Marque `repo` (acesso completo aos repositórios)
4. Clique em **"Generate token"**
5. **COPIE O TOKEN** (não será mostrado novamente!)
6. Use o token como senha ao fazer push

### Opção 2: GitHub Desktop

Baixe e use o GitHub Desktop para facilitar:
https://desktop.github.com/

## ✅ Verificar

Após o push, acesse seu repositório:
```
https://github.com/SEU_USUARIO/BocaoLanches
```

Você deve ver todos os arquivos do projeto lá!

## 🚀 Próximo Passo

Depois que o repositório estiver no GitHub:
1. Volte ao Render
2. Na tela de criar serviço web
3. Selecione seu repositório `BocaoLanches`
4. Continue com a configuração

---

## 🆘 Problemas Comuns

### Erro: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin SUA_URL_AQUI
```

### Erro de autenticação
- Use Personal Access Token em vez de senha
- Ou configure SSH keys

### Arquivos não aparecem no GitHub
```powershell
git add .
git commit -m "Adicionar arquivos"
git push -u origin main
```
