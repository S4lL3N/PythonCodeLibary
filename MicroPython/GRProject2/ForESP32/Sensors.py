import Log
import Drivers.seesaw as seesaw
import Drivers.StemmaSoilSensor as StemmaSoilSensor
import dht
from machine import Pin, I2C
import machine
import Helper

import esp32



def getData(plant):  
    dht11Readings = getDHT11TempAndHum()
    tempInF = dht11Readings[0]
    humidity = dht11Readings[1]
    stemmaReadings = getStemmaMoistureAndTemp()
    soilMoisture = stemmaReadings[0]
    soilTemp = stemmaReadings[1]


    results = [tempInF, humidity, soilMoisture, soilTemp, plant] 
    Log.LogToSheets(results)
    return results
    
'''
# logs data using the IFTTT webhooks method
    resultsForIFTTT = [tempInF, humidity, soilMoisture]
    Log.logToSheetsIFTTT(resultsForIFTTT)
'''

def getDHT11TempAndHum():
    sensor = Pin(15,Pin.IN)
    d = dht.DHT11(sensor)
    d.measure()
    tempInC = d.temperature()
    tempInF = str( 9 / 5 * tempInC + 32)
    humidity = str(d.humidity()) # add the -5 to match the other sensor in room and the dht11 is +/- 5
    dht11Results = [tempInF, humidity]
    return dht11Results

def getStemmaMoistureAndTemp():
    #https://github.com/mihai-dinculescu/micropython-adafruit-drivers/tree/master/seesaw
    SDA_PIN = 5 # update this
    SCL_PIN = 4 # update this

    sensorRangeLow = 650 # dry
    sensorRangeHigh = 783 # wet

    i2c = machine.I2C(sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
    #-----------------------------------------------------------------------------------------------------
    #to get the avg of 10 readings (hoping to get more accurate reading)
    i = 0
    total = 0
    while i < 10:
        soilMoistureRaw = StemmaSoilSensor.StemmaSoilSensor(i2c).get_moisture()
        total += soilMoistureRaw 
        i+=1
    
    soilMoistureRaw = total / 10
    #----------------------------------------------------------------------------------------------------

    #soilMoistureRaw = StemmaSoilSensor.StemmaSoilSensor(i2c).get_moisture()
    soilMoisture = Helper.ChangeRange(sensorRangeLow, sensorRangeHigh, soilMoistureRaw)

    #soilTempInC = StemmaSoilSensor.StemmaSoilSensor(i2c).get_temp()
    #soilTempInF = str( 9 / 5 * soilTempInC + 32)

    stemmaResults = [soilMoisture,  soilMoistureRaw]

    return stemmaResults

def esp32Sensors():
    import esp32
    esp32temp = esp32.raw_temperature()
    esp32Hall = esp32.hall_sensor() 
    return esp32temp


def led(led, state):
    LED_BLUE = machine.Pin(13, machine.Pin.OUT)
    LED_GREEN = machine.Pin(12, machine.Pin.OUT)
    LED_YELLOW = machine.Pin(14, machine.Pin.OUT)
    LED_RED = machine.Pin(2, machine.Pin.OUT)
    if led == "blue" and state == "ON":
        LED_BLUE.on()
    if led == "blue" and state == "OFF":
        LED_BLUE.off()
    if led == "green" and state == "ON":
        LED_GREEN.on()
    if led == "green" and state == "OFF":
        LED_GREEN.off()
    if led == "yellow" and state == "ON":
        LED_YELLOW.on()
    if led == "yellow" and state == "OFF":
        LED_YELLOW.off()
    if led == "red" and state == "ON":
        LED_RED.on()
    if led == "red" and state == "OFF":
        LED_RED.off()

    
