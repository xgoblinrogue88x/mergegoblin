@echo off
setlocal EnableExtensions
rem PUSHD temporarily maps UNC shares; CD cannot use them as working folders.
pushd "%~dp0"
if errorlevel 1 goto folder_failed

rem Keep executable dependencies local, even when the app/videos live on a NAS.
if not defined LOCALAPPDATA goto no_local_folder
set "MG_ENV=%LOCALAPPDATA%\MergeGoblin\venv"
set "MG_ENV_PY=%MG_ENV%\Scripts\python.exe"
if exist "%MG_ENV_PY%" goto check_environment

set "MG_PYTHON="
set "MG_PY_ARGS="
call :try_python py -3
if not defined MG_PYTHON call :try_python python
if not defined MG_PYTHON call :try_python python3
rem Also find standard installations that were not added to PATH.
for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python*") do if not defined MG_PYTHON if exist "%%~fD\python.exe" call :try_python "%%~fD\python.exe"
for /d %%D in ("%ProgramFiles%\Python*") do if not defined MG_PYTHON if exist "%%~fD\python.exe" call :try_python "%%~fD\python.exe"
if not defined MG_PYTHON goto missing_python

echo Creating the local Python environment...
"%MG_PYTHON%" %MG_PY_ARGS% -m venv "%MG_ENV%"
if errorlevel 1 goto failed

:check_environment
"%MG_ENV_PY%" -c "import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)" >nul 2>nul
if errorlevel 1 goto environment_failed
"%MG_ENV_PY%" -c "import tkinter; import venv" >nul 2>nul
if errorlevel 1 goto missing_tk
"%MG_ENV_PY%" -m pip install --upgrade -r requirements.txt
if errorlevel 1 goto failed
"%MG_ENV_PY%" mergegoblin.py wizard
if errorlevel 1 goto failed
popd
pause
exit /b 0

:try_python
"%~1" %~2 -c "import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)" >nul 2>nul
if errorlevel 1 exit /b 0
set "MG_PYTHON=%~1"
set "MG_PY_ARGS=%~2"
exit /b 0

:missing_python
echo.
echo Python 3.12 or newer was not found.
echo Install Python from https://www.python.org/downloads/windows/
echo In the installer, enable Add python.exe to PATH and include Tcl/Tk.
echo Or run this in PowerShell: winget install --id Python.Python.3.12 --exact
echo After installing, double-click Start.bat again.
goto failed

:missing_tk
echo This Python installation is missing Tcl/Tk or venv support.
echo Modify your Python installation to include Tcl/Tk, then rerun Start.bat.
goto failed

:environment_failed
echo The saved Python environment is unavailable or older than Python 3.12.
echo Rename this application's environment folder, then rerun Start.bat:
echo "%MG_ENV%"
goto failed

:no_local_folder
echo Windows did not provide a LOCALAPPDATA folder for the Python environment.
goto failed

:folder_failed
echo Unable to open the app folder. Check the network share connection.
echo You can also extract the app into a local folder such as Downloads.
pause
exit /b 1

:failed
echo.
echo Setup or processing stopped. Read the error above. Your source videos were not removed.
popd
pause
exit /b 1
