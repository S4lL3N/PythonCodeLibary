from time import sleep
import RPi.GPIO as GPIO
import subprocess as sub

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while 1:
        if GPIO.input(12) == 0:
                print("button was pressed")
                sleep(.1)
                sub.call(['python', 'test.py'])

       