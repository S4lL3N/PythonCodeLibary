import cv2 as cv
import numpy as np
from PIL import ImageGrab
import pyautogui

class WindowCapture:

    def capture():
        # without bbox it grabs my whole screen
        screen = np.array(ImageGrab.grab(bbox=(35,176,836,775))) 
        new_screen = WindowCapture.convert_img(screen)
        new_screen = cv.cvtColor(screen, cv.COLOR_BGR2RGB)
        return new_screen

    def getScreenshot():
        pic = pyautogui.screenshot(region=((45,181,844,780))) # first two points are the top left corner of square the last to are the bottom right corner.
        width, height = pic.size
        return pic, width, height