from pynput import mouse
import os, pyautogui
import pystray
from pystray import Menu, MenuItem
from PIL import Image
import platform
import keyboard


def exit_action(icon):
    icon.stop()
    os._exit(1)


def copyToClipboard():
    if platform.system() == "Windows":
        if keyboard.is_pressed("Ctrl"):
            pyautogui.hotkey('Ctrl', 'c')
            

    # if platform.system == "Darwin":
    #     pyautogui.hotkey('command', 'c')


def pasteFromClipboard():
    if platform.system() == "Windows":
        if keyboard.is_pressed("Ctrl"):
            pyautogui.hotkey('Ctrl', 'v')
            

    # if platform.system == "Darwin":
    #     pyautogui.hotkey('command', 'v')
        

def on_click(x, y, button, pressed):
    #print('{0} {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

    if pressed and button == mouse.Button.left:
        copyToClipboard()

    if pressed and button == mouse.Button.right:
        pasteFromClipboard()


if __name__ == '__main__':
    image = Image.open("icon.ico")

    icon = pystray.Icon('Mighty Mouse')
    icon.menu = Menu(
        MenuItem('Close Mighty Mouse', lambda : exit_action(icon)),
    )
    icon.icon = image
    icon.title = 'Mighty Mouse 1.0.1'

    with mouse.Listener(on_click = on_click) as listener:
        icon.run()
        listener.join()

    