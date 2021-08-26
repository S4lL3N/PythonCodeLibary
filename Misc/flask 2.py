from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return 'fuck off'


@app.route('/garage', methods=['GET', 'POST'])
def gDoorOpen():
    subprocess.call(['python', 'FlaskGarageDoor.py'])
    return "the script ran"

@app.route('/Singlegarage', methods=['GET', 'POST'])
def DoorOpen():
    subprocess.call(['python', 'FlaskSingleGarageDoor.py'])
    return "the script ran"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)