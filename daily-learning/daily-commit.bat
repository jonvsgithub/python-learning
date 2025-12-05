@echo off
REM Daily Python Learning Commit Scheduler
REM This batch file is run by Windows Task Scheduler daily

cd /d "C:\Users\HP\OneDrive\Notes\PYTHON"

REM Set execution policy for PowerShell
powershell -ExecutionPolicy RemoteSigned -File "daily-learning\daily-commit-automation.ps1" -Topic "Daily Python Learning Commit"

REM Log the execution
echo [%date% %time%] Daily learning commit executed >> daily-learning\commit-log.txt
