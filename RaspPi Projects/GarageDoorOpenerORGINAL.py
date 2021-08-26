#!/usr/bin/python3
import RPi.GPIO as GPIO
import time


def openDoor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    time.sleep(2)
    GPIO.cleanup()
    time.sleep(20)   # Door takes 12 seconds to open.


for x in range(1, 3):
    total = str(x)
    print(total)
    openDoor()
    if total == '1':
        print("Garage door now: OPEN")
        print(total)
    if total == '2':
        print("\nGarage door now: CLOSED")
        print(total)
        time.sleep(15)
        print("\nNow exiting program")


