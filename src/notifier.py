import subprocess
from logger import log

def notify(title: str, msg: str):
    """
    Envía una notificación Toast en Windows usando PowerShell.

    Args:
        title (str): Título de la notificación.
        msg (str): Mensaje de la notificación.
    """
    powershell_script = f'''[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
$textNodes = $template.GetElementsByTagName("text")
$textNodes.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null
$textNodes.Item(1).AppendChild($template.CreateTextNode("{msg}")) > $null
$toast = [Windows.UI.Notifications.ToastNotification]::new($template)
$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("SSMS Discord RPC")
$notifier.Show($toast)
'''
    try:
        subprocess.Popen(["powershell", "-NoProfile", "-Command", powershell_script], shell=True)
    except Exception as e:
        log(f"Error mostrando notificación: {e}")
