@echo off
chcp 65001 >nul
color 0B
title RIVAL STRESS - ADMIN

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
title RIVAL STRESS - Ultra Premium Stress Engine
cd /d "%~dp0"
cls
echo.
echo ═══════════════════════════════════════════════════════════════
echo                    ⚡ RIVAL STRESS ⚡
echo                   Developed by ADAZ_TR
echo ═══════════════════════════════════════════════════════════════
echo.
echo [🛡️] Yönetici modu aktif!
echo.

python rival_stress.py

if %errorlevel% neq 0 (
    echo.
    echo ═══════════════════════════════════════════════════════════════
    echo                         ❌ HATA!
    echo ═══════════════════════════════════════════════════════════════
    echo.
    echo Script çalıştırılamadı. Olası nedenler:
    echo   - Python kurulu değil
    echo   - rival_stress.py bulunamadı
    echo   - Dosya izinleri sorunu
    echo.
    echo Çözüm için INSTALL.bat dosyasını çalıştırın.
    echo.
    pause
    exit /b 1
)

echo.
pause
