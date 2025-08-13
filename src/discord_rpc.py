import time
import traceback
from pypresence import Presence, DiscordNotFound, InvalidPipe
from utils.logger import log

CLIENT_ID = "1404602960700379267"  # Cambia por tu ID de aplicación de Discord
LARGE_IMAGE_KEY = "imagen_2025-08-12_014439804"  # Clave de la imagen en la app Discord

def safe_disconnect(rpc):
    """
    Limpia la conexión Discord RPC de forma segura.
    Args:
        rpc: instancia de Presence o None
    """
    try:
        if rpc:
            try:
                rpc.clear()
            except:
                pass
            try:
                rpc.close()
            except:
                pass
    except:
        pass

class DiscordRPCManager:
    """
    Clase para manejar la conexión y presencia con Discord RPC.
    """
    def __init__(self, client_id=CLIENT_ID):
        self.client_id = client_id
        self.rpc = None
        self.presence_active = False

    def connect(self) -> bool:
        """
        Intenta conectar con Discord RPC.
        Returns:
            bool: True si la conexión fue exitosa, False si falló.
        """
        try:
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            self.presence_active = True
            log("RPC conectado y presencia activada.")
            return True
        except DiscordNotFound:
            log("Discord desktop no encontrado. Esperando...")
        except InvalidPipe:
            log("InvalidPipe al conectar RPC. Reiniciando estado RPC.")
        except Exception as e:
            log(f"Error al conectar RPC: {type(e).__name__} - {e}")
            traceback.print_exc()
        self.presence_active = False
        self.rpc = None
        return False

    def update_presence(self, details="Querying in SQL Server", state="Database: AdventureWorks2022") -> bool:
        """
        Actualiza el estado en Discord si está conectado.
        Args:
            details (str): Detalles de la presencia.
            state (str): Estado de la presencia.
        Returns:
            bool: True si la actualización fue exitosa, False si falló.
        """
        if self.presence_active and self.rpc:
            try:
                self.rpc.update(
                    details=details,
                    state=state,
                    large_image=LARGE_IMAGE_KEY,
                    start=int(time.time())
                )
                return True
            except Exception as e:
                log(f"Error al actualizar presencia: {e}")
                return False
        return False

    def disconnect(self):
        """
        Desconecta y limpia el estado RPC.
        """
        safe_disconnect(self.rpc)
        self.rpc = None
        self.presence_active = False
        log("RPC desconectado y presencia limpiada.")
