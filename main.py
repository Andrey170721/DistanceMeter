import time
from pynput.mouse import Listener
import math

SHIFT = False
CALIBRATION = False
F = True
FIRST_X = 0
FIRST_Y = 0
SECOND_X = 0
SECOND_Y = 0
SCALE = 0
ONE_METER = 52


def on_click(x, y, button, pressed):
    global SHIFT
    global F
    global CALIBRATION
    global SCALE
    global FIRST_X
    global FIRST_Y
    global SECOND_X
    global SECOND_Y
    global ONE_METER
    if pressed and CALIBRATION:
        if F:
            print("Нажмите на второй угол квадрата")
            FIRST_X = x
            FIRST_Y = y
        else:
                SECOND_X = x
                SECOND_Y = y
                CALIBRATION = False
                d = math.sqrt((FIRST_X - SECOND_X) ** 2 + (FIRST_Y - SECOND_Y) ** 2) / 52
                ONE_METER = d / SCALE
                print("Калибровка завершена")
                CALIBRATION = False
                SHIFT = True
        F = not F
    else:
        if pressed and SHIFT:
            if F:
                FIRST_X = x
                FIRST_Y = y
                print(f"{x}, {y}")
            if not F:
                SECOND_X = x
                SECOND_Y = y
                print(f"{x}, {y}")

            d = (math.sqrt((FIRST_X - SECOND_X)**2 + (FIRST_Y - SECOND_Y)**2) / 52) / ONE_METER
            print("Расстояние: ", d)
            F = not F


def on_press(key):
    global SHIFT
    global F
    if key == keyboard.KeyCode.from_char('l'):
        SHIFT = not SHIFT
    if key == keyboard.KeyCode.from_char('p'):
        global CALIBRATION
        global SCALE
        print("Введите масштаб: ")
        SCALE = float(input())
        F = True
        CALIBRATION = True
        print("Нажмите на первый угол квадрата")

from pynput import keyboard

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

with Listener(on_click=on_click) as listener:
    listener.join()
