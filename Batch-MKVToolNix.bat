@echo off
setlocal EnableExtensions
pushd "%~dp0"
if errorlevel 1 goto folder_failed
set "MG_PY=%LOCALAPPDATA%\MergeGoblin\venv\Scripts\python.exe"
if not exist "%MG_PY%" goto missing_python
if not exist "work\plan.json" goto missing_plan
echo Batch mode: append complete compatible episodes without encoding or resizing.
echo Originals stay in their existing folders. Incompatible episodes are held.
"%MG_PY%" mkv_batch.py %*
set "MG_RESULT=%ERRORLEVEL%"
if not "%MG_RESULT%"=="0" echo Some episodes were held or processing failed. Read batch-summary.txt or the error above.
popd
pause
exit /b %MG_RESULT%
:missing_python
echo Run Start.bat once to set up Python, then close it before starting this batch.
goto finished
:missing_plan
echo Copy your existing work folder into this app folder before starting the batch.
:finished
popd
pause
exit /b 1
:folder_failed
echo Cannot open the app folder. Check the share connection or use a local folder.
pause
exit /b 1
