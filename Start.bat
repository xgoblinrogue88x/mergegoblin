@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Install Python 3.12 or newer from python.org, including the Python launcher.
  pause
  exit /b 1
)
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m pip install --upgrade -r requirements.txt
if errorlevel 1 goto failed
.venv\Scripts\python.exe mergegoblin.py wizard
if errorlevel 1 goto failed
pause
exit /b 0
:failed
echo Setup or processing failed. Read the error above. Your source videos were not removed.
pause
exit /b 1
