@echo off
setlocal EnableExtensions
pushd "%~dp0"
if errorlevel 1 goto folder_failed
set "MG_PY=%LOCALAPPDATA%\MergeGoblin\venv\Scripts\python.exe"
if not exist "%MG_PY%" goto missing_python
if not exist "work\plan.json" goto missing_plan
"%MG_PY%" e01_mkvmerge.py
set "MG_RESULT=%ERRORLEVEL%"
if not "%MG_RESULT%"=="0" echo E01 was not accepted automatically. Read the result and log shown above.
popd
pause
exit /b %MG_RESULT%
:missing_python
echo Run Start.bat once to set up Python, then close it before testing E01.
goto finished
:missing_plan
echo Copy your existing work folder into this app folder before testing E01.
:finished
popd
pause
exit /b 1
:folder_failed
echo Cannot open the app folder. Check the share connection or use a local folder.
pause
exit /b 1
