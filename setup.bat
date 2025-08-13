@echo off
echo Instalando dependencias para Windows...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Instalacion completada.
echo Para iniciar el programa, ejecuta: python src\main.py
pause
