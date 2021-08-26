import requests as req

temp = "70"
hum = "50"

data = "http://127.0.0.1:4200/sensor_readings?" + "temperature=" + temp + "&humidity=" + hum
req.post(data)