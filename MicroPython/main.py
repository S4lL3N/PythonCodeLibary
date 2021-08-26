import internet
import time
import webServer
from machine import Pin, I2C
import ssd1306



# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(4), sda=Pin(5))
relay = Pin(17, Pin.IN)

# oled variables
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Repl and Oled display booting  up
time.sleep(3)
print("\n\nBooting UP....")
oled.text('Booting up....', 0, 0)
oled.show()
time.sleep(2)

# Connecting to the internet
print("connecting to internet...\n")
print("\nConnected: ", internet.connect())
oled.init_display()
oled.text('Connected:', 0, 0)
oled.text(internet.ip, 0, 10)
oled.show()

# starting the web server 
time.sleep(1)
print("\nStarting S4lL3N's webServer....\n")
oled.text('Webserver = True', 0, 40)
oled.show()
webServer.startServer()




