from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
log = open("log.txt", 'w')


def main():
    if GPIO.input(12) == 0:
        print("button was pressed")
        print("button was pressed", file=log)
        sleep(.1)
        subprocess.call(['python', 'test.py'])


main()