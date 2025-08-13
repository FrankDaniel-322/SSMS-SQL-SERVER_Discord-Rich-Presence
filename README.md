# SSMS SQL SERVER - Discord Rich Presence

Proyecto para mostrar en Discord la presencia cuando SQL Server Management Studio (SSMS) está activo, usando Discord Rich Presence y notificaciones nativas en Windows.

---

## Autor

    ElPsyCongroo

---

## Contenido

- **src/**: Código fuente organizado por módulos.
- **requirements.txt**: Dependencias Python necesarias.
- **setup.bat**: Script para instalación automática en Windows.
- **setup.sh**: Script para instalación automática en Mac/Linux.
- **README.md**: Este archivo.

---

## Funcionalidades

- Detecta si SSMS está abierto.
- Actualiza el estado de Discord con información personalizada.
- Notificaciones nativas de Windows usando PowerShell.
- Manejo robusto de errores y reconexiones.
- Código modular y listo para extenderse a otros programas.

---

## Requisitos

- Python 3.8 o superior
- Discord Desktop app abierta y sesión iniciada
- Windows 10/11 (para notificaciones nativas con PowerShell)
- Permisos para ejecutar scripts PowerShell (en Windows)

---

## Instalación

### 1. Clona el repositorio

Abre la terminal, da permisos de ejecución y ejecuta el script:

    git clone https://github.com/FrankDaniel-322/SSMS-SQL-SERVER_Discord-Rich-Presence.git
    cd ssms-discord-rpc

### 2. Instala dependencias

- Windows
Ejecuta en la consola

    setup.bat

- Mac/Linux
En el terminal:

    chmod +x setup.sh
    ./setup.sh

---

### Uso

Ejecuta el programa principal:

- Windows
Ejecuta en la consola:
    python src\main.py

- Mac/Linux
En el terminal:
    python3 src/main.py

---

### Estructura del proyecto
```
ssms-discord-rpc/
│
├── src/
│   ├── __init__.py            # Inicialización del paquete
│   ├── main.py                # Script principal que ejecuta la aplicación
│   ├── notifier.py            # Módulo para mostrar notificaciones nativas
│   ├── presence_manager.py    # Gestión del estado y conexión con Discord RPC
│   ├── utils.py               # Funciones auxiliares como logging y detección de procesos
│
├── requirements.txt           # Dependencias Python
├── setup.bat                  # Instalador automático para Windows
├── setup.sh                   # Instalador automático para Mac/Linux
├── README.md                  # Documentación del proyecto
└── .gitignore                 # Archivos a ignorar en Git
```

---

## Personalización

 - Cambia 'CLIENT_ID' en 'src
 - Cambia 'PROCESS_NAME' en 'src/process_watcher.py' si quieres monitorear otro proceso.
 - Cambia 'LARGE_IMAGE_KEY' en 'src/discord_rpc.py' por la clave de imagen que tengas en tu app Discord.

---

## Detalles técnicos

 - Las notificaciones se muestran usando PowerShell Toast Notifications en Windows 10/11.

 - La conexión con Discord usa la librería pypresence.

---

## Licencia

MIT License © 2025 ElPsyCongroo

---

### ¡Gracias por usar SSMS Discord RPC!
