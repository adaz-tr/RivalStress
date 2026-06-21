@echo off
chcp 65001 >nul
color 0B
title RIVAL STRESS - KURULUM

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
cd /d "%~dp0"
cls
echo.
echo ═══════════════════════════════════════════════════════════════
echo                    ⚡ RIVAL STRESS ⚡
echo                  Kurulum Kontrol Scripti
echo                   Developed by ADAZ_TR
echo ═══════════════════════════════════════════════════════════════
echo.

echo [1/3] Python sürümü kontrol ediliyor...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python bulunamadı!
    echo.
    echo Lütfen Python 3.8+ yükleyin:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

python --version
echo ✅ Python kurulu!
echo.

echo [2/3] Gerekli modüller kontrol ediliyor...
echo.
echo Tüm modüller Python standart kütüphanesinde!
echo ✅ socket
echo ✅ threading
echo ✅ time
echo ✅ sys
echo ✅ datetime
echo ✅ os
echo ✅ ctypes
echo.

echo [3/3] Script dosyası kontrol ediliyor...
if exist "rival_stress.py" (
    echo ✅ rival_stress.py bulundu!
) else (
    echo ❌ rival_stress.py bulunamadı!
    echo.
    echo Lütfen dosyanın aynı klasörde olduğundan emin olun.
    pause
    exit /b 1
)
echo.

echo ═══════════════════════════════════════════════════════════════
echo                     ✅ KURULUM TAMAMLANDI!
echo ═══════════════════════════════════════════════════════════════
echo.
echo RIVAL STRESS kullanmaya hazır!
echo.
echo Başlatmak için:
echo   python rival_stress.py
echo.
echo veya RUN.bat dosyasını çalıştırın
echo.
pause
