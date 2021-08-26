import urequests

def logToSheets(sensorData):
    sensor_readings = sensorData
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post('https://maker.ifttt.com/trigger/DHT11_Readings/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn',
    json=sensor_readings,
    headers=request_headers)
    #print(request.text)
    request.close()


 






