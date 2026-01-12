# ⚠️ Python Não Encontrado

Parece que o Python não está instalado ou não está no PATH do sistema.

## 🔧 Solução Rápida

### Opção 1: Instalar Python (Recomendado)

1. **Baixe o Python:**
   - Acesse: https://www.python.org/downloads/
   - Baixe a versão mais recente (3.11 ou 3.12)

2. **Durante a instalação:**
   - ✅ **MARQUE A OPÇÃO**: "Add Python to PATH"
   - ✅ Marque também: "Install pip"
   - Clique em "Install Now"

3. **Após instalar:**
   - Feche e reabra o PowerShell
   - Execute: `python --version` para verificar

### Opção 2: Usar Python já instalado

Se você já tem Python instalado mas não está no PATH:

1. Encontre onde o Python está instalado (geralmente em):
   - `C:\Python3x\`
   - `C:\Program Files\Python3x\`
   - `C:\Users\Administrador\AppData\Local\Programs\Python\Python3x\`

2. Use o caminho completo:
   ```powershell
   C:\Python3x\python.exe -m venv venv
   ```

3. Ou adicione ao PATH:
   - Painel de Controle > Sistema > Variáveis de Ambiente
   - Adicione o caminho do Python ao PATH

## ✅ Verificar Instalação

Execute o script de verificação:
```powershell
.\verificar_python.ps1
```

## 🚀 Após Instalar Python

Depois que o Python estiver instalado, execute:

```powershell
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente virtual
.\venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar migrações
python manage.py makemigrations
python manage.py migrate

# 5. Criar superusuário
python manage.py createsuperuser

# 6. Executar servidor
python manage.py runserver
```

## 📞 Precisa de Ajuda?

Se continuar com problemas, verifique:
- Python está instalado? Execute: `python --version`
- Está no PATH? Execute: `where.exe python`
- Tentou reiniciar o PowerShell após instalar?
