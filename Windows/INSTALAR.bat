@echo off
rem Caminho absoluto do proprio .bat: chamada relativa falha nesta maquina.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar.ps1"
if errorlevel 1 pause
