import webbrowser
import pyautogui
from time import sleep

  

telefones = [xxxxxxxxxxx, xxxxxxxxxxxxx, xxxxxxxxxx]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(501,907, duration=1)
    pyautogui.typewrite("Ola, automatizando whatsapp, gracias.")
    sleep(5)
    pyautogui.press('enter')
    sleep(20)

