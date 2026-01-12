@echo off
REM Script batch para executar o servidor Django
REM Use este arquivo se o PowerShell nao funcionar

cd /d "%~dp0"

echo === Iniciando Servidor Bocao Lanches ===
echo.

if not exist "manage.py" (
    echo ERRO: Execute este script na pasta do projeto!
    pause
    exit /b 1
)

if not exist "venv\Scripts\python.exe" (
    echo ERRO: Ambiente virtual nao encontrado!
    echo Execute primeiro: configurar_projeto.ps1
    pause
    exit /b 1
)

echo Iniciando servidor Django...
echo.
echo URLs disponiveis:
echo   Site: http://127.0.0.1:8000
echo   Admin: http://127.0.0.1:8000/admin
echo   Dashboard: http://127.0.0.1:8000/dashboard/
echo.
echo Credenciais:
echo   Username: admin
echo   Password: admin123
echo.
echo Pressione CTRL+C para parar o servidor
echo.

venv\Scripts\python.exe manage.py runserver
