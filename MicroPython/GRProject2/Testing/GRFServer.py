from flask import Flask, request, jsonify
import LogToSheet as log

app = Flask(__name__)

@app.route('/api/sensor_readings', methods=['GET', 'POST'])
def sensor_readings():    
    content = request.json
    print("Temperature= " + str(content['temp']))
    temp = str(content['temp'])
    print("Humidity= " + str(content['hum']))
    humidity = str(content['hum'])
    print("SoilMoisture= " + str(content['soilMoist']))
    soilMoisture =str(content['soilMoist'])
    print("SoilTemperature= " + str(content['soilTemp']))
    soilTemp = str(content['soilTemp'])

    
    log.googleSheetsLog(temp,humidity, soilMoisture, soilTemp)
    return "Succesfully Logged"

if __name__ == '__main__':
    app.run(host= '192.168.1.10',port='4200',debug=True)