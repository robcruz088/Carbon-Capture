import serial
import json
from time import time
from random import random
from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    # Temperature = random() * 100
    # Humidity = random() * 55

    with open("sensor.json", 'r') as f:
        sensor_data = json.load(f)

    temp_c = sensor_data["Temperature(C/F)"][0]
    temp = str(random() * 100)
    hum = sensor_data["Humidity(%)"]
    co = sensor_data["CO(ppm)"]
    small = sensor_data["PM_Small"]
    large = sensor_data = ["PM_Large"]
    print(co)

    send_data = [time() * 1000, temp_c, hum, co, small, large]

    response = make_response(json.dumps(send_data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)