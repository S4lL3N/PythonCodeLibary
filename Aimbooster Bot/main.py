from ControlIO import ControlIO as CIO
import cv2 as cv
import time
from WindowCapture import WindowCapture 
from ColorDetect import colorDetect 
import keyboard

#This program is a aimbot for http://www.aimbooster.com/

def main():
    #to get mouse position and RGB values of pixel.
    #CIO.readMouseLoc()

    print("\nStarting Aim bot...")
    time.sleep(1)
    print("Pressing Start...")
    CIO.mouseClick(654, 738) #cords of the start button.
    print("Running...")
    print("\nPress Q to Quit.")

    while keyboard.is_pressed('q') == False:
        screenshot, width, height = WindowCapture.getScreenshot()
        colorDetect.findColor(screenshot, width, height)

       
if __name__ == "__main__":
    main()