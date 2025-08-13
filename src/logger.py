from datetime import datetime

def log(msg):
    """
    Imprime mensaje con timestamp.
    Args:
        msg (str): Mensaje a imprimir.
    """
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
