@echo off
:: ================================================
::  STUDY MODE — Auto-start (Fixed: no CMD window
::  dependency, process survives CMD closing)
::  Krish Baral
:: ================================================

:: ── Re-launch as Administrator if not already ──
net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -WindowStyle Hidden -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /b
)

:: ── Config ──────────────────────────────────────
set SCRIPT=%~dp0study_mode_krish.py

:: Uncomment and set your exact Python path if needed:
:: set PYTHONW=C:\Users\Krish\AppData\Local\Programs\Python\Python312\pythonw.exe

:: ── Find pythonw automatically ───────────────────
:: pythonw.exe = same as python.exe but NO console window at all
for /f "delims=" %%i in ('where pythonw 2^>nul') do set PYTHONW=%%i
if not defined PYTHONW (
    for /f "delims=" %%i in ('where python 2^>nul') do (
        set PYTHONW=%%~dpi\pythonw.exe
    )
)

:: ── Check script exists ──────────────────────────
if not exist "%SCRIPT%" (
    powershell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('study_mode_krish.py not found next to BAT file.','StudyMode Error')"
    exit /b 1
)

:: ── Install dependencies silently if missing ─────
python -c "import plyer,pystray,PIL,keyboard,pygame,openpyxl" >nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install plyer pystray pillow keyboard pygame openpyxl --quiet
)

:: ── Register startup task (once, safe to repeat) ─
::    Points to .vbs so Task Scheduler shows no CMD
schtasks /query /tn "StudyModeKrish" >nul 2>&1
if %errorlevel% neq 0 (
    schtasks /create /tn "StudyModeKrish" /tr "wscript.exe \"%~dp0StudyMode_Silent.vbs\"" /sc ONLOGON /rl HIGHEST /f /delay 0000:30 >nul
)

:: ── Launch using pythonw (detached, no console) ───
::    pythonw = python but zero console window
::    Process is fully independent — closing CMD does nothing to it
if defined PYTHONW (
    start "" /B "%PYTHONW%" "%SCRIPT%"
) else (
    powershell -WindowStyle Hidden -Command "Start-Process python -ArgumentList '\"%SCRIPT%\"' -WindowStyle Hidden"
)

exit /b 0
