# Whatsapp MOD

import pyautogui,webbrowser
from time import sleep
"""
Abre el whatsapp web y envia un mensaje a el numero ingresado
"""
webbrowser.open('https://web.whatsapp.com/send?phone=+573227531696')
sleep(15) # Espera para cargar la pagina y ejecutar el bucle
for i in range(100):
    pyautogui.typewrite("No me rete") # Texto que se va a enviar
    pyautogui.press('enter') # Evento de dar enter para enviar mensaje