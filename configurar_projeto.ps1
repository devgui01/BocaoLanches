# Script de Configuracao Automatica do Projeto Bocao Lanches
Write-Host "=== Configuracao do Projeto Bocao Lanches ===" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "1. Verificando Python..." -ForegroundColor Yellow
$pythonCmd = $null

# Tentar diferentes comandos Python
$pythonCommands = @("python", "python3", "py")
foreach ($cmd in $pythonCommands) {
    try {
        $result = & $cmd --version 2>&1
        if ($LASTEXITCODE -eq 0 -or $result -match "Python") {
            $pythonCmd = $cmd
            Write-Host "   Python encontrado: $cmd" -ForegroundColor Green
            & $cmd --version
            break
        }
    } catch {
        continue
    }
}

if (-not $pythonCmd) {
    Write-Host "   ERRO: Python nao encontrado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor, instale o Python primeiro:" -ForegroundColor Yellow
    Write-Host "1. Acesse: https://www.python.org/downloads/" -ForegroundColor Cyan
    Write-Host "2. Baixe e instale a versao mais recente" -ForegroundColor Cyan
    Write-Host "3. IMPORTANTE: Marque 'Add Python to PATH' durante a instalacao" -ForegroundColor Yellow
    Write-Host "4. Feche e reabra o PowerShell" -ForegroundColor Yellow
    Write-Host "5. Execute este script novamente" -ForegroundColor Yellow
    exit 1
}

# Verificar se estamos no diretorio correto
if (-not (Test-Path "manage.py")) {
    Write-Host "ERRO: Arquivo manage.py nao encontrado!" -ForegroundColor Red
    Write-Host "Certifique-se de estar na pasta do projeto" -ForegroundColor Yellow
    exit 1
}

# Criar arquivo .env se nao existir
Write-Host ""
Write-Host "2. Verificando arquivo .env..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    Write-Host "   Criando arquivo .env..." -ForegroundColor Green
    @"
SECRET_KEY=django-insecure-change-this-in-production-12345
DEBUG=True
MERCADOPAGO_ACCESS_TOKEN=
INSTAGRAM_ACCESS_TOKEN=
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "   Arquivo .env criado!" -ForegroundColor Green
} else {
    Write-Host "   Arquivo .env ja existe" -ForegroundColor Green
}

# Criar ambiente virtual
Write-Host ""
Write-Host "3. Criando ambiente virtual..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "   Ambiente virtual ja existe" -ForegroundColor Green
} else {
    & $pythonCmd -m venv venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   Ambiente virtual criado!" -ForegroundColor Green
    } else {
        Write-Host "   ERRO ao criar ambiente virtual" -ForegroundColor Red
        exit 1
    }
}

# Ativar ambiente virtual
Write-Host ""
Write-Host "4. Ativando ambiente virtual..." -ForegroundColor Yellow
$activateScript = "venv\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    & $activateScript
    Write-Host "   Ambiente virtual ativado!" -ForegroundColor Green
} else {
    Write-Host "   ERRO: Script de ativacao nao encontrado" -ForegroundColor Red
    exit 1
}

# Instalar dependencias
Write-Host ""
Write-Host "5. Instalando dependencias..." -ForegroundColor Yellow
& $pythonCmd -m pip install --upgrade pip
& $pythonCmd -m pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "   Dependencias instaladas!" -ForegroundColor Green
} else {
    Write-Host "   ERRO ao instalar dependencias" -ForegroundColor Red
    exit 1
}

# Criar diretorios necessarios
Write-Host ""
Write-Host "6. Criando diretorios..." -ForegroundColor Yellow
$dirs = @("static", "media", "media\produtos")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "   Diretorio $dir criado" -ForegroundColor Green
    }
}

# Executar migracoes
Write-Host ""
Write-Host "7. Executando migracoes do banco de dados..." -ForegroundColor Yellow
& $pythonCmd manage.py makemigrations
& $pythonCmd manage.py migrate
if ($LASTEXITCODE -eq 0) {
    Write-Host "   Migracoes executadas!" -ForegroundColor Green
} else {
    Write-Host "   ERRO ao executar migracoes" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Configuracao Concluida! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Proximos passos:" -ForegroundColor Cyan
Write-Host "1. Criar superusuario: $pythonCmd manage.py createsuperuser" -ForegroundColor White
Write-Host "2. Executar servidor: $pythonCmd manage.py runserver" -ForegroundColor White
Write-Host "3. Acessar: http://127.0.0.1:8000" -ForegroundColor White
Write-Host ""
