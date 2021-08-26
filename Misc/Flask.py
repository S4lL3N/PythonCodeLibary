from flask import Flask
import pigpio


pigpio.exceptions = False
piOG = pigpio.pi('192.168.1.9')

if not piOG.connected:
    print("Connection Failed!")
    exit()

app = Flask(__name__)

@app.route('/')
def index():
    return "fuck off"


@app.route('/garage', methods=['GET', 'POST'])
def gDoorOpen():
    piOG.set_mode(4, pigpio.OUTPUT)
    time.sleep(2)
    print("Garage Door Opening!")
    piOG.set_mode(4, pigpio.INPUT)
    time.sleep(20)
    piOG.set_mode(4, pigpio.OUTPUT)
    time.sleep(2)
    print("Garage Door Closing!")
    piOG.set_mode(4, pigpio.INPUT)
    piOG.stop()
    print("Now Exiting Program!")
    return "the script ran"




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)