import serial # pyserial library for serial data from arduino
import pymongo
import datetime
import random
import string
import json


# client = pymongo.MongoClient("mongodb+srv://SensorUser:camdenlab@testcluster.dzoyl.mongodb.net/sensor_data?retryWrites=true&w=majority")
# db = client["sensor_data"] # database in the mongodb cluster
# db_collection = db["sensor"] # collection in the dataabase

# library that contains the sensor data, using JSON notation for pymongo collection
sensor_data = {"Temperature(C/F)": ["",""],
         "Humidity(%)": "",
         "CO(ppm)": "",
         "timmestamp": "",
         "_id": ""
        }

# db_collection.insert_one(sensor_data)

arduinoData = serial.Serial('com3', 9600) # serial object with corresponding port and baud rate

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))


while True:
    while (arduinoData.inWaiting() == 0): #wait here until there is data
        pass
    arduinoString = arduinoData.readline().decode('utf-8').strip() #convert data into a string
    dataArray = arduinoString.split(',')

    # convert string values to int
    temp_c = int(dataArray[0])
    temp_f = int(dataArray[1])
    hum = int(dataArray[2])
    co = float(dataArray[3])

    # update dict values
    sensor_data["Temperature(C/F)"][0] = temp_c
    sensor_data["Temperature(C/F)"][1] = temp_f
    sensor_data["Humidity(%)"] = hum
    sensor_data["CO(ppm)"] = co
    sensor_data["timmestamp"] = str(datetime.datetime.now())
    sensor_data["_id"] = id_generator()

    with open("sensor.json", 'w') as f:
            json.dump(sensor_data,f, indent=2)

    ## TODO: Change Collection to a couple of seconds / minute intervals
    #db_collection.insert_one(sensor_data) # insert a new document each iteration

    #r = request.post("http://127.0.0.1:5000/", bson=sensor_data)

    print(sensor_data)

