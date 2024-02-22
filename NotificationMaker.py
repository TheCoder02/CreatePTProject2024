from plyer import *
from PIL import Image
import pyautogui
from Graphics import *
import socket
   
   
def ip():
   hostname = socket.gethostname()
   ip_address = socket.gethostbyname(hostname)
   print(f"Hostname: {hostname}")
   print(f"IP Address: {ip_address}")


def virusClick():
   notification.notify(
      title = 'Target Sale',
      message = 'Don\'t miss these weekly ad deals.',
      app_icon = 'targetlogo.ico',
      timeout = 10,
   )

