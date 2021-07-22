from data_collector import *

# global variable
collect = data_collection("sensor.json")

def temperature_collector():
    temp_dict = collect.search("Temperature(C/F)")
    return temp_dict


def humitidy_collector():
    humidity = collect.search("Humidity(%)")
    return humidity

def co_collector():
    co = collect.search("CO(ppm)")
    return co

