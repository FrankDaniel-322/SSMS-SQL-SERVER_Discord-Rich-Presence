import time
import sys
from core.process_watcher import ssms_window_running
from core.discord_rpc import DiscordRPCManager
from core.notifier import notify
from utils.logger import log

CHECK_INTERVAL = 2  # segundos

def main():
    log("Iniciando vigilante SSMS Discord RPC.")
    notify("SSMS Discord RPC", "Vigilante iniciado.")

    rpc_manager = DiscordRPCManager()

    try:
        while True:
            running = ssms_window_running()

            if running and not rpc_manager.presence_active:
                log("Ssms.exe detectado -> intentando conectar RPC...")
                if rpc_manager.connect():
                    rpc_manager.update_presence()
                    notify("SSMS Discord RPC", "SQL Server detectado y conectado a Discord.")
            elif not running and rpc_manager.presence_active:
                log("Ssms.exe ya no está -> limpiando presencia...")
                rpc_manager.disconnect()
                notify("SSMS Discord RPC", "SQL Server cerrado, presencia limpiada.")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        log("Interrupción por teclado, saliendo...")
    except Exception as e:
        log(f"Error inesperado: {e}")
    finally:
        rpc_manager.disconnect()
        log("Servicio detenido.")
        sys.exit(0)

if __name__ == "__main__":
    main()
