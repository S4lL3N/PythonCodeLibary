from machine import Pin
import dht
import urequests

def getData():
    sensor = Pin(17,Pin.IN)
    d = dht.DHT11(sensor)
    d.measure()
    tempInC = d.temperature()
    tempInF = str( 9 / 5 * tempInC + 32)
    hum = str(d.humidity() - 5 ) # add the -5 to match the other sensor in room and the dht11 is +/- 5
    soil = ""
    #print("temp= " + tempInF + " Hum= " + hum)

    sensor_readings = {'value1':tempInF, 'value2':hum, 'value3':soil}

    #print(sensor_readings)

    request_headers = {'Content-Type': 'application/json'}

    request = urequests.post('https://maker.ifttt.com/trigger/DHT11_Readings/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn',
    json=sensor_readings,
    headers=request_headers)
    #print(request.text)
    request.close()


