from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

while True:
    mouse.press(Button.left)
    mouse.release(Button.left)
