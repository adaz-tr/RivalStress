@echo off
chcp 65001 >nul
color 0A
title RIVAL CHECKER - ADMIN

:: Yönetici kontrolü
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :admin
) else (
    echo.
    echo [🛡️] Yönetici izni alınıyor...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:admin
chcp 65001 >nul
title RIVAL PACKET RECEIVER - Live Capture
cd /d "%~dp0"
cls
echo.
echo ═══════════════════════════════════════════════════════════════
echo                📡 RIVAL PACKET RECEIVER 📡
echo                   Developed by ADAZ_TR
echo ═══════════════════════════════════════════════════════════════
echo.
echo [🛡️] Yönetici modu aktif!
echo.

python receiver_check.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Hata oluştu!
    pause
)

echo.
pause
