from flask import Flask, request, jsonify
import LogToSheet as log

app = Flask(__name__)

@app.route('/api/sensor_readings', methods=['GET', 'POST'])
def sensor_readings():
    content = request.json
    #print("Temperature= " + str(content['temp']))
    temp = content['temp']
    #print("Humidity= " + str(content['hum']))
    humidity = content['hum']
    #print("SoilMoisture= " + str(content['soilMoist']))
    soilMoisture =content['soilMoist']
    #print("SoilTemperature= " + str(content['soilTemp']))
    soilTemp = content['soilTemp']
    #print("plant= " + str(content['plant']))
    plant = content['plant']
    
    log.googleSheetsLog(temp,humidity, soilMoisture, soilTemp, plant)
    
    return "Succesfully Logged"
    

if __name__ == '__main__':
    app.run(host= '192.168.1.10',port='4200',debug=True)
