# 🖼️ Como Adicionar a Logo da Empresa

## 📍 Localização

Coloque o arquivo da logo na pasta:
```
static/images/logo.png
```

## 📝 Passos

### 1. Preparar a Logo

- **Formato recomendado**: PNG com fundo transparente
- **Tamanho navbar**: 150x50px (proporção 3:1)
- **Tamanho página inicial**: 400x200px ou maior
- **Qualidade**: Alta resolução para melhor visualização

### 2. Adicionar o Arquivo

1. Copie sua logo para a pasta `static/images/`
2. Renomeie para `logo.png` (ou ajuste o código se usar outro nome)
3. Formatos aceitos: PNG, JPG, SVG

### 3. Atualizar Arquivos Estáticos

Execute no terminal:
```powershell
python manage.py collectstatic --noinput
```

### 4. Verificar

- Acesse: http://127.0.0.1:8000
- A logo deve aparecer:
  - No navbar (canto superior esquerdo)
  - Na página inicial (centro da página)

## 🎨 Onde a Logo Aparece

1. **Navbar** - Canto superior esquerdo de todas as páginas
2. **Página Inicial** - Centro da página, grande e destacada

## 🔧 Personalização

### Se usar outro nome de arquivo:

Edite `templates/base.html` e `templates/core/index.html`:

```html
<!-- Troque: -->
{% static 'images/logo.png' %}

<!-- Por: -->
{% static 'images/seu-arquivo.extensao' %}
```

### Ajustar tamanho:

Edite `static/css/bocao_style.css`:

```css
/* Logo navbar */
.logo-navbar {
    height: 50px;  /* Ajuste aqui */
    max-width: 150px;  /* Ajuste aqui */
}

/* Logo principal */
.logo-principal {
    max-width: 400px;  /* Ajuste aqui */
}
```

## ❓ Problemas Comuns

### Logo não aparece:

1. ✅ Verifique se o arquivo está em `static/images/logo.png`
2. ✅ Execute: `python manage.py collectstatic`
3. ✅ Limpe o cache do navegador (Ctrl+F5)
4. ✅ Verifique o console do navegador (F12) para erros

### Logo muito grande/pequena:

- Ajuste os valores em `bocao_style.css` (veja seção Personalização)

### Logo com fundo branco:

- Use PNG com fundo transparente
- Ou edite a logo removendo o fundo

## 📱 Responsividade

A logo se ajusta automaticamente em dispositivos móveis:
- Navbar: reduz para 40px de altura
- Página inicial: reduz para 280px de largura

## ✨ Efeitos Aplicados

A logo recebe automaticamente:
- Sombra para destaque
- Efeito hover (aumenta levemente)
- Animação de entrada na página inicial
- Ajuste automático de tamanho

---

**Dica**: Use uma logo de alta qualidade para melhor resultado em todos os tamanhos!
