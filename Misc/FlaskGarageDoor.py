#!/usr/bin/python3
import pigpio
import time

pigpio.exceptions = False
piOG = pigpio.pi('192.168.1.9')

if not piOG.connected:
    print("Connection Failed!")
    exit()

def main():
    piOG.set_mode(4, pigpio.OUTPUT)
    time.sleep(2)
    print("Garage Door Opening!")
    piOG.set_mode(4, pigpio.INPUT)
    time.sleep(20)
    piOG.set_mode(4, pigpio.OUTPUT)
    time.sleep(2)
    print("Garage Door Closing!")
    piOG.set_mode(4, pigpio.INPUT)
    piOG.stop()
    print("Now Exiting Program!")


main()