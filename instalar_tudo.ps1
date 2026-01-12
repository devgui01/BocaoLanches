# Script Completo de Instalacao e Configuracao do Projeto Bocao Lanches
# Este script tenta instalar Python e configurar tudo automaticamente

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  INSTALACAO AUTOMATICA - BOCAO LANCHES" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se estamos no diretorio correto
if (-not (Test-Path "manage.py")) {
    Write-Host "ERRO: Execute este script na pasta do projeto!" -ForegroundColor Red
    Write-Host "Diretorio atual: $(Get-Location)" -ForegroundColor Yellow
    pause
    exit 1
}

# Funcao para verificar Python
function Test-PythonInstalled {
    $pythonCommands = @("python", "python3")
    foreach ($cmd in $pythonCommands) {
        try {
            $version = & $cmd --version 2>&1
            if ($version -match "Python (\d+)\.(\d+)") {
                return @{Command = $cmd; Version = $version; Found = $true}
            }
        } catch {
            continue
        }
    }
    return @{Found = $false}
}

# Verificar Python
Write-Host "[1/8] Verificando Python..." -ForegroundColor Yellow
$pythonCheck = Test-PythonInstalled

if (-not $pythonCheck.Found) {
    Write-Host "   Python nao encontrado. Tentando instalar..." -ForegroundColor Yellow
    
    # Tentar instalar via winget
    $wingetAvailable = $false
    try {
        $wingetVersion = winget --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $wingetAvailable = $true
            Write-Host "   Winget encontrado. Instalando Python..." -ForegroundColor Cyan
            winget install Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
            Start-Sleep -Seconds 5
            
            # Atualizar PATH
            $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
            
            # Verificar novamente
            Start-Sleep -Seconds 2
            $pythonCheck = Test-PythonInstalled
        }
    } catch {
        Write-Host "   Winget nao disponivel" -ForegroundColor Yellow
    }
    
    if (-not $pythonCheck.Found) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Red
        Write-Host "  PYTHON NAO ENCONTRADO!" -ForegroundColor Red
        Write-Host "========================================" -ForegroundColor Red
        Write-Host ""
        Write-Host "Por favor, instale o Python manualmente:" -ForegroundColor Yellow
        Write-Host "1. Acesse: https://www.python.org/downloads/" -ForegroundColor Cyan
        Write-Host "2. Baixe e instale Python 3.11 ou superior" -ForegroundColor Cyan
        Write-Host "3. IMPORTANTE: Marque 'Add Python to PATH'" -ForegroundColor Yellow
        Write-Host "4. Feche e reabra o PowerShell" -ForegroundColor Yellow
        Write-Host "5. Execute este script novamente" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Ou execute: .\configurar_projeto.ps1" -ForegroundColor Cyan
        Write-Host ""
        pause
        exit 1
    }
}

Write-Host "   Python encontrado: $($pythonCheck.Version)" -ForegroundColor Green
$pythonCmd = $pythonCheck.Command

# Criar arquivo .env
Write-Host ""
Write-Host "[2/8] Configurando arquivo .env..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    @"
SECRET_KEY=django-insecure-change-this-in-production-$(Get-Random -Minimum 10000 -Maximum 99999)
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
Write-Host "[3/8] Criando ambiente virtual..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "   Ambiente virtual ja existe. Removendo..." -ForegroundColor Yellow
    Remove-Item -Path "venv" -Recurse -Force
}
& $pythonCmd -m venv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "   ERRO ao criar ambiente virtual" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "   Ambiente virtual criado!" -ForegroundColor Green

# Ativar ambiente virtual
Write-Host ""
Write-Host "[4/8] Ativando ambiente virtual..." -ForegroundColor Yellow
$activateScript = "venv\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    & $activateScript
    # Usar Python do venv
    $pythonCmd = "venv\Scripts\python.exe"
    Write-Host "   Ambiente virtual ativado!" -ForegroundColor Green
} else {
    Write-Host "   ERRO: Script de ativacao nao encontrado" -ForegroundColor Red
    pause
    exit 1
}

# Atualizar pip
Write-Host ""
Write-Host "[5/8] Atualizando pip..." -ForegroundColor Yellow
& $pythonCmd -m pip install --upgrade pip --quiet
Write-Host "   pip atualizado!" -ForegroundColor Green

# Instalar dependencias
Write-Host ""
Write-Host "[6/8] Instalando dependencias (isso pode levar alguns minutos)..." -ForegroundColor Yellow
& $pythonCmd -m pip install -r requirements.txt --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "   ERRO ao instalar dependencias" -ForegroundColor Red
    Write-Host "   Tentando novamente sem modo silencioso..." -ForegroundColor Yellow
    & $pythonCmd -m pip install -r requirements.txt
}
Write-Host "   Dependencias instaladas!" -ForegroundColor Green

# Criar diretorios
Write-Host ""
Write-Host "[7/8] Criando diretorios necessarios..." -ForegroundColor Yellow
$dirs = @("static", "media", "media\produtos")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}
Write-Host "   Diretorios criados!" -ForegroundColor Green

# Executar migracoes
Write-Host ""
Write-Host "[8/8] Configurando banco de dados..." -ForegroundColor Yellow
& $pythonCmd manage.py makemigrations --noinput 2>&1 | Out-Null
& $pythonCmd manage.py migrate --noinput
if ($LASTEXITCODE -eq 0) {
    Write-Host "   Banco de dados configurado!" -ForegroundColor Green
} else {
    Write-Host "   ERRO ao configurar banco de dados" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  INSTALACAO CONCLUIDA COM SUCESSO!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Proximos passos:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Criar usuario administrador:" -ForegroundColor White
Write-Host "   .\venv\Scripts\python.exe manage.py createsuperuser" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. Executar servidor:" -ForegroundColor White
Write-Host "   .\venv\Scripts\python.exe manage.py runserver" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. Acessar no navegador:" -ForegroundColor White
Write-Host "   Site: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "   Admin: http://127.0.0.1:8000/admin" -ForegroundColor Cyan
Write-Host ""
Write-Host "Deseja criar o usuario administrador agora? (S/N)" -ForegroundColor Yellow
$resposta = Read-Host
if ($resposta -eq "S" -or $resposta -eq "s") {
    Write-Host ""
    Write-Host "Siga as instrucoes na tela para criar o usuario..." -ForegroundColor Cyan
    & $pythonCmd manage.py createsuperuser
}

Write-Host ""
Write-Host "Deseja executar o servidor agora? (S/N)" -ForegroundColor Yellow
$resposta = Read-Host
if ($resposta -eq "S" -or $resposta -eq "s") {
    Write-Host ""
    Write-Host "Iniciando servidor..." -ForegroundColor Cyan
    Write-Host "Acesse: http://127.0.0.1:8000" -ForegroundColor Green
    Write-Host "Pressione CTRL+C para parar o servidor" -ForegroundColor Yellow
    Write-Host ""
    & $pythonCmd manage.py runserver
}
