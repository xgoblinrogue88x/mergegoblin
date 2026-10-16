@echo off
setlocal EnableExtensions
pushd "%~dp0"
if errorlevel 1 goto folder_failed
set "LFDH_PY=%LOCALAPPDATA%\MergeGoblin\venv\Scripts\python.exe"
if not exist "%LFDH_PY%" goto missing_python
if not exist "work\plan.json" goto missing_plan
echo Creating episode folders with ordered playlists. Original videos stay untouched.
"%LFDH_PY%" episode_playlists.py %*
set "LFDH_RESULT=%ERRORLEVEL%"
if not "%LFDH_RESULT%"=="0" echo Some episodes were held. Read the error or playlist-summary.txt.
popd
pause
exit /b %LFDH_RESULT%
:missing_python
echo The existing MergeGoblin Python environment was not found. Run Start.bat to set it up first.
goto finished
:missing_plan
echo Copy your existing work folder into this app folder before running this launcher.
:finished
popd
pause
exit /b 1
:folder_failed
echo Cannot open the app folder. Check its network connection or use a local folder.
pause
exit /b 1
