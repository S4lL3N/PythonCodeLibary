from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

keyboard = KeyboardController()
mouse = MouseController()

mouse.position = (1223, 664)
keyboard.press('F')