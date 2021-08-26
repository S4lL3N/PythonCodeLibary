import internet
import utime
#import TempHum as th
import Sensors

utime.sleep(3)
print("\n\nBooting UP....")

print("connecting to internet...\n")
print("\nConnected: ", internet.connect())

notDone = True
while(notDone):
    #th.getData()
    Sensors.getData()
    count = 5400 # for 8 readings a day or every 3 hours
    while count > 0:
        utime.sleep(2)
        count -= 1

