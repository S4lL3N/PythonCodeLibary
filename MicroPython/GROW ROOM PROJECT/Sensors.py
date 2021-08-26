from machine import Pin
import dht
import Log

def getData():
    sensor = Pin(17,Pin.IN)
    d = dht.DHT11(sensor)
    d.measure()
    tempInC = d.temperature()
    tempInF = str( 9 / 5 * tempInC + 32)
    humidity = str(d.humidity() - 5 ) # add the -5 to match the other sensor in room and the dht11 is +/- 5
    soilMoisture = ""
    soilTemp = ""
    #print("temp= " + tempInF + " Hum= " + humidity)

    sensor_readings = {'value1':tempInF, 'value2':humidity, 'value3':soilMoisture}
    #print(sensor_readings)
    
    Log.logToSheets(sensor_readings)



