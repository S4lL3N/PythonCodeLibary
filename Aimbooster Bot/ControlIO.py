import pyautogui
import pydirectinput
import pynput
import win32api, win32con
import time

class ControlIO:

    #read mouse location and RGB values.
    @staticmethod
    def readMouseLoc():
        pyautogui.displayMousePosition()

    @staticmethod
    def mouseClick(x, y):
        #pyautogui.click(x, y)
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)