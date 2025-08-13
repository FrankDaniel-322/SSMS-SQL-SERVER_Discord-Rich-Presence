import psutil

PROCESS_NAME = "Ssms.exe"

def ssms_window_running() -> bool:
    """
    Devuelve True si existe un proceso con nombre EXACTO igual a 'Ssms.exe'.

    Returns:
        bool: True si el proceso está corriendo, False si no.
    """
    for p in psutil.process_iter(['name']):
        try:
            if p.info.get('name') == PROCESS_NAME:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False
