from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

'''
def on_press(key):
    try:
        key = '{0}'.format(key.char)
    except:
        key = ''
    if key == 'p':
        mouse.press(Button.left)
        mouse.release(Button.left)
    #通过属性判断按键类型。

def on_release(key):
    key = '{0}'.format(key)
    if key == 'p':
        mouse.release(Button.left)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
'''
while True:
    mouse.press(Button.left)
    mouse.release(Button.left)
