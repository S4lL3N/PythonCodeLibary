import Sensors
import urequests
import time
logSuccess =None 
#######################################################################################################################################
moistAlert = 10
#######################################################################################################################################
def logToSheetsIFTTT(sensorData):
    sensor_readings = {'value1':sensorData[0],
                       'value2':sensorData[1],
                       'value3':sensorData[2]}
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post('https://maker.ifttt.com/trigger/DHT11_Readings/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn',
    json=sensor_readings,
    headers=request_headers)
    #print(request.text)
    request.close()

def LogToSheets(sensonReadings):
    temp = sensonReadings[0]
    hum = sensonReadings[1]
    soilMoist = sensonReadings[2]
    soilTemp = sensonReadings[3]
    plant = sensonReadings[4]
    payload = {"temp":temp,
                "hum":hum,
                "soilMoist":soilMoist,
                "soilTemp":soilTemp,
                "plant":plant}
    while(True):
        try:
            request_headers = {'Content-Type': 'application/json'}
            res = urequests.post('http://192.168.1.10:4200/api/sensor_readings', 
            json=payload,
            headers=request_headers)
            response = res.text
            res.close()
            if response == "Succesfully Logged":
                #print(res.json())
                print("Request was successful")
                global logSuccess 
                logSuccess = True
                break
            else:
                print("***FAILED***")
                time.sleep(10)
                global logSuccess
                logSuccess = False
                continue
        except Exception as e:
            print('Error...')
            print(e)

    if soilMoist < moistAlert:
        #IFTTT_SMS(plant, soilMoist)
        pass

    if soilMoist < 33.3:
        Sensors.led("red","ON")
        Sensors.led("green","OFF")
        Sensors.led("yellow","OFF")
    if soilMoist > 33.3 and soilMoist < 66.6:
        Sensors.led("red","OFF")
        Sensors.led("green","OFF")
        Sensors.led("yellow","ON")
    if soilMoist > 66.6:
        Sensors.led("red","OFF")
        Sensors.led("green","ON")
        Sensors.led("yellow","OFF")

def IFTTT_SMS(plant, soilMoisture):
    report = {}
    report["value1"] = plant
    report["value2"] = soilMoisture
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post('https://maker.ifttt.com/trigger/GR_SMS/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn',
    json=report,
    headers=request_headers)
    #print(request.text)
    request.close()


 






