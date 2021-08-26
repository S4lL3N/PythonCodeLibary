
from flask import Flask, request, jsonify
import LogToSheet as log

app = Flask(__name__)

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print(content['temp'])
    temp = str(content['temp'])
    print(content['hum'])
    humidity = str(content['hum'])
    print(content['soilMoist'])
    soilMoisture =str(content['soilMoist'])
    print(content['soilTemp'])
    soilTemp = str(content['soilTemp'])

    #print(content)
    log.googleSheetsLog(temp,humidity, soilMoisture, soilTemp)
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '192.168.1.10',port='4200',debug=True)
