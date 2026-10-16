@echo off
setlocal EnableExtensions
pushd "%~dp0"
if errorlevel 1 goto folder_failed
set "LFDH_PY=%LOCALAPPDATA%\MergeGoblin\venv\Scripts\python.exe"
set "LFDH_PY_ARGS="
if exist "%LFDH_PY%" goto run_sort
set "LFDH_PY="
call :try_python python
if not defined LFDH_PY call :try_python py -3
if not defined LFDH_PY call :try_python python3
if not defined LFDH_PY goto missing_python
:run_sort
echo Select the folder containing your 290 videos.
echo This MOVES them into episode subfolders. It does not change their filenames or contents.
"%LFDH_PY%" %LFDH_PY_ARGS% sort_episodes.py %*
set "LFDH_RESULT=%ERRORLEVEL%"
popd
pause
exit /b %LFDH_RESULT%
:try_python
"%~1" %~2 -c "import tkinter" >nul 2>nul
if errorlevel 1 exit /b 0
set "LFDH_PY=%~1"
set "LFDH_PY_ARGS=%~2"
exit /b 0
:missing_python
echo Python with Tcl/Tk was not found. Install Python from https://www.python.org/downloads/windows/
echo Enable Add python.exe to PATH and include Tcl/Tk, then run this launcher again.
popd
pause
exit /b 1
:folder_failed
echo Cannot open the app folder. Check the share connection or use a local folder.
pause
exit /b 1
