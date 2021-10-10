import pyautogui
from ControlIO import ControlIO as CIO
import time

class colorDetect:
    
    def findColor(capture, width, height):
        
        for x in range(0,width,5):
            for y in range(0,height,5):
                r, g, b, = capture.getpixel((x, y))
                #target_color = (255,219,195) check for B value
                if b == 195:
                    CIO.mouseClick(x+45, y+181) # add the starting points of screenshot
                    time.sleep(.06)
                    break
