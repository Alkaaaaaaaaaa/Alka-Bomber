@echo off

set PYTHON_EXECUTABLE=python.exe

set SCRIPT_FILE=Alka-Bomber.py

if not exist "%PYTHON_EXECUTABLE%" (
  echo Error: Python executable not found at %PYTHON_EXECUTABLE%
  exit /b 1
)

if not exist "%SCRIPT_FILE%" (
  echo Error: Script file not found at %SCRIPT_FILE%
  exit /b 1
)

"%PYTHON_EXECUTABLE%" "%SCRIPT_FILE%" %*
