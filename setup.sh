#!/bin/bash
echo "Instalando dependencias para Mac/Linux..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
echo "Instalacion completada."
echo "Para iniciar el programa, ejecuta: python3 src/main.py"
