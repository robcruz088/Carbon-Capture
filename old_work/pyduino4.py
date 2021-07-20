import serial                                               #import pyserial library
import numpy                                                #import numpy
import matplotlib.pyplot as plt                             #import matplotlib library
from drawnow import *                                       #import drawnow library
from datetime import datetime                                      #import time library
#from serial import Serial

temp = []                                                   #temperature array
hum = []                                                    #humidity array
co = []                                                     #carbon monoxide array
no2 = []                                                     #nitrogen dioxide array 
small = []                                                  #small Particulate Matter array
big = []                                                    #large particulate matter array
arduinoData = serial.Serial('com3', 9600)                   #creating serial object name arduinoData
plt.ion()                                                   #Tell matplotlib user wants interactive mode to plot live data
cnt = 0                                                     #counter starter
start_time = datetime.now()

def makeFig():                                              #create a function that makes the plot
    figure(1)
    plt.title('Humidity % vs Time')
    plt.grid(True)
    plt.ylim(0,100)
    plt.ylabel('Humidity %')
    plt.xlabel('Time (s)')
    plt.plot(hum, 'b-')
    figure(2)
    plt.title('Temperature (F) vs Time')
    plt.grid(True)
    plt.ylim(32,122)
    plt.ylabel('Temperature (F)')
    plt.xlabel('Time (s)')
    plt.plot(temp,'r-')
    figure(3)
    plt.title('Carbon Monoxide vs Time')                    #creating all of the graphs 
    plt.grid(True)
    plt.ylim(0,100)
    plt.ylabel('CO (PPM)')
    plt.xlabel('Time(s)')
    plt.plot(co,'g-')
    figure(4)
    plt.title('Small PM and Large PM vs Time')
    plt.grid(True)
    plt.ylim(0,20)
    plt.ylabel('small PM2.5 (PPM)')
    plt.xlabel('Time (s)')
    plt.plot(small,'y-')
    plt2 = plt.twinx()
    plt.ylim(0,20)
    plt2.set_ylabel('Large PM10 (PPM)')
    plt2.plot(big,'g-')
    figure(5)
    plt.title("Nitrogen Dioxide Levels vs Time")
    plt.grid(True)
    plt.ylim(0,300)
    plt.ylabel('NO2 (PPB)')
    plt.xlabel('Time (s)')
    plt.plot(no2,'k-')
       

while True:                                                 #while loop that loops forever
    while (arduinoData.inWaiting() == 0):                   #wait here until there is data
        pass                                                #do nothing
    
    arduinoString = arduinoData.readline().decode('utf-8').strip() #convert data into a string
    dataArray = arduinoString.split(',')                    #data as an array, split the string at the comma 
    T = float(dataArray[0])                                 #convert first element to a floating number
    H = float(dataArray[1])                                 #convert second element to a floating number
    C = float(dataArray[2])                                 #convert third element to a floating number
    S = float(dataArray[3])                                 #convert fourth element to a floating number
    B = float(dataArray[4])                                 #convert fifth element to a floating number 
    N = float(dataArray[5])                                 #convert sixth element to a floating number 
    temp.append(T)                                          #build temp array by appending T readings
    hum.append(H)                                           #build hum array by appendig H readings
    co.append(C)                                            #build CO array 
    small.append(S)                                         #build small PM array
    big.append(B)                                           #build large PM array
    no2.append(N)                                           #build NO2 array
    drawnow(makeFig)                                        #call drawnow to update our live graph
    plt.pause(.000001)                                      #a small pause 
    cnt = cnt + 1                                           #adds one to the counter called earlier
    if (cnt > 30):                                          #after enough additions, if the counter is above 30
        temp.pop(0)                                         #pop out the number at the 0 label and effectively 
        hum.pop(0)               
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
