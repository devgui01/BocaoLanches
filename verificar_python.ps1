# Script para verificar e configurar Python
Write-Host "=== Verificando Instalacao do Python ===" -ForegroundColor Cyan

# Verificar python
$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if ($pythonPath) {
    Write-Host "Python encontrado em: $($pythonPath.Source)" -ForegroundColor Green
    python --version
} else {
    Write-Host "Python nao encontrado no PATH" -ForegroundColor Yellow
    
    # Verificar locais comuns
    $commonPaths = @(
        "C:\Python*",
        "C:\Program Files\Python*",
        "C:\Program Files (x86)\Python*",
        "$env:LOCALAPPDATA\Programs\Python\Python*"
    )
    
    Write-Host "`nProcurando Python em locais comuns..." -ForegroundColor Cyan
    $found = $false
    foreach ($path in $commonPaths) {
        $pythonDirs = Get-ChildItem -Path $path -ErrorAction SilentlyContinue -Directory
        foreach ($dir in $pythonDirs) {
            $pythonExe = Join-Path $dir.FullName "python.exe"
            if (Test-Path $pythonExe) {
                Write-Host "Python encontrado em: $pythonExe" -ForegroundColor Green
                & $pythonExe --version
                $found = $true
                Write-Host "`nPara usar este Python, execute:" -ForegroundColor Yellow
                Write-Host "& '$pythonExe' -m venv venv" -ForegroundColor White
                break
            }
        }
        if ($found) { break }
    }
    
    if (-not $found) {
        Write-Host "`nPython nao encontrado!" -ForegroundColor Red
        Write-Host "Por favor, instale o Python de:" -ForegroundColor Yellow
        Write-Host "https://www.python.org/downloads/" -ForegroundColor Cyan
        Write-Host "`nIMPORTANTE: Marque a opcao 'Add Python to PATH' durante a instalacao!" -ForegroundColor Yellow
    }
}

Write-Host "`n=== Verificando pip ===" -ForegroundColor Cyan
$pipPath = Get-Command pip -ErrorAction SilentlyContinue
if ($pipPath) {
    Write-Host "pip encontrado!" -ForegroundColor Green
    pip --version
} else {
    Write-Host "pip nao encontrado" -ForegroundColor Yellow
}
