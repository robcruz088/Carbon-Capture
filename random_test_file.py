from flask import Flask, render_template, redirect, url_for, request
import requests
import datetime
import json
import pymongo
from functools import partial
from json import JSONDecoder

# if __name__ == '__main__':
#     client = pymongo.MongoClient("mongodb+srv://SensorUser:camdenlab@testcluster.dzoyl.mongodb.net/sensor_data?retryWrites=true&w=majority")
#     db = client["sensor_data"]  # database in the mongodb cluster
#     db_collection = db["sensor"] # collection in the dataabase
#     cursor = db_collection.find({})
#     for document in cursor:
#           print(document)

# client = pymongo.MongoClient("mongodb+srv://SensorUser:camdenlab@testcluster.dzoyl.mongodb.net/sensor_data?retryWrites=true&w=majority")
# db = client["sensor_data"] # database in the mongodb cluster
# db_collection = db["sensor"] # collection in the dataabase
#
# cursor = db_collection.find({})
# with open("sensor.json",'w') as f:
#     for document in cursor:
#         json.dump(document, f, indent=4)
#     #print(document)
#
# def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
#     """ JSON Parser function"""
#     buffer = ''
#     for chunk in iter(partial(fileobj.read, buffersize), ''):
#          buffer += chunk
#          while buffer:
#              try:
#                  result, index = decoder.raw_decode(buffer)
#                  yield result
#                  buffer = buffer[index:].lstrip()
#              except ValueError:
#                  # Not enough data to decode, read more
#                  break

# with open('sensor.json', 'r') as infh:
#     for data in json_parse(infh):
#         print(data)

with open('sensor.json', 'r') as f:
    data = json.load(f)

print(type(data))