# Script para executar o servidor Django
# Use este script sempre que quiser iniciar o servidor

Write-Host "=== Iniciando Servidor Bocao Lanches ===" -ForegroundColor Cyan
Write-Host ""

# Verificar se estamos no diretorio correto
if (-not (Test-Path "manage.py")) {
    Write-Host "ERRO: Execute este script na pasta do projeto!" -ForegroundColor Red
    pause
    exit 1
}

# Verificar se ambiente virtual existe
if (-not (Test-Path "venv\Scripts\python.exe")) {
    Write-Host "ERRO: Ambiente virtual nao encontrado!" -ForegroundColor Red
    Write-Host "Execute primeiro: .\configurar_projeto.ps1" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "Iniciando servidor Django..." -ForegroundColor Yellow
Write-Host ""
Write-Host "URLs disponiveis:" -ForegroundColor Cyan
Write-Host "  Site: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "  Admin: http://127.0.0.1:8000/admin" -ForegroundColor White
Write-Host "  Dashboard: http://127.0.0.1:8000/dashboard/" -ForegroundColor White
Write-Host ""
Write-Host "Credenciais:" -ForegroundColor Cyan
Write-Host "  Username: admin" -ForegroundColor White
Write-Host "  Password: admin123" -ForegroundColor White
Write-Host ""
Write-Host "Pressione CTRL+C para parar o servidor" -ForegroundColor Yellow
Write-Host ""

# Executar servidor
.\venv\Scripts\python.exe manage.py runserver
