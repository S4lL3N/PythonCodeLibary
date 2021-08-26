import internet
import Log
import Sensors
import Helper
import utime
from machine import Pin, I2C
from Drivers import ssd1306
import gc

########################################################################################################################################
#PLANT = "Plant#1"
#Pid = 1
PLANT = "Plant#2" #stemma sensor might need calibrating.
Pid = 2
#PLANT = "Plant#3"
#Pid = 3
#PLANT = "Plant#4"
#Pid = 4

SSID = 'S4lL3N-2.4Ghz'
PASSWORD = 'mangosgetyouhigher'
######################################################################################################################################

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(4), sda=Pin(5))

# oled variables
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Repl and Oled display booting  up
utime.sleep(3)
print("\n\nBooting UP....")
oled.text('Booting up....', 0, 0)
oled.show()
utime.sleep(2)

# Connecting to the internet
print("connecting to internet...\n")
print("\nConnected: ", internet.connect(SSID,PASSWORD))
oled.init_display()
oled.text('Connected:     '+ str(Pid), 0, 0)
oled.text(internet.ip, 0, 10)
oled.show()

gc.enable()
utime.sleep(1)
forEver = True
while(forEver):
    connected = internet.check()
    while(connected):
        Sensors.led("blue","ON")
        oled.init_display()
        readings = Sensors.getData(PLANT)    
        #print("\nSending Log request....\n")
        oled.text('Sending Log...', 0, 20)
        oled.show()
        if Log.logSuccess == True:
            oled.text('Successful!', 0, 30)
            oled.show()
            oled.text('Loading...', 0, 40)
            oled.show()
        else:
            oled.text('failed', 0, 30)
            oled.show()
        timer = 1080 # in 10 second increments, so 1080 * 10  = 10800 seconds or 3 hours for for 8 readings a day.
        #timer = 18 # every 3 minutes
        while timer > 0:
            utime.sleep(10)
            timer -= 1
            oled.init_display()
            oled.text('Connected:     '+ str(Pid), 0, 0)
            oled.text(internet.ip, 0, 10)
            countDown = Helper.countToTime(timer)
            oled.text('Update In: '+ countDown, 0, 30)
            oled.text('T=' + str(readings[0]) + ',' + 'H='+ str(readings[1]), 0, 40)
            oled.text('SM=' + str(round(readings[2],1)) + ',' + 'ST='+ str(readings[3]), 0, 50)
            oled.show()

    Sensors.led("blue", "OFF")
    oled.init_display()
    oled.text('Lost Connection...', 0, 0)
    oled.text('Reconnecting now...', 0, 10) 
    oled.show()       
    internet.connect()
        
