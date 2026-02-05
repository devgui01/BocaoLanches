# 🖼️ IMPORTANTE: Como Adicionar a Logo Corretamente

## ⚠️ Problema Detectado

O arquivo `logo.png` está **VAZIO** (0 bytes). Isso significa que você criou o arquivo mas não adicionou a imagem.

## ✅ Solução

### Passo 1: Obter a Logo
- Tenha o arquivo da logo da empresa em formato PNG, JPG ou SVG

### Passo 2: Adicionar a Logo
1. Abra a pasta: `C:\Users\Administrador\BocaoLanches\static\images\`
2. **DELETE** o arquivo `logo.png` vazio (se existir)
3. **COPIE** sua logo para esta pasta
4. **RENOMEIE** para `logo.png` (ou mantenha o nome se já for .png)

### Passo 3: Verificar
O arquivo deve ter tamanho maior que 0 bytes. Para verificar:
```powershell
cd C:\Users\Administrador\BocaoLanches
Get-Item static\images\logo.png | Select-Object Name, Length
```

### Passo 4: Atualizar
```powershell
python manage.py collectstatic --noinput
```

### Passo 5: Recarregar
- Pressione `Ctrl + F5` no navegador para limpar cache
- A logo deve aparecer no lugar do ícone de café

## 📍 Onde a Logo Aparece

1. **Navbar** - No lugar do ícone de café (canto superior esquerdo)
2. **Página Inicial** - Grande e centralizada

## 🎨 Formatos Aceitos

- PNG (recomendado - com fundo transparente)
- JPG
- SVG

## 📏 Tamanhos Recomendados

- **Navbar**: 150x50px (proporção 3:1)
- **Página inicial**: 400x200px ou maior

## ❓ Ainda não aparece?

1. Verifique se o arquivo não está vazio
2. Verifique o nome: deve ser exatamente `logo.png`
3. Limpe o cache: `Ctrl + F5`
4. Execute: `python manage.py collectstatic`
