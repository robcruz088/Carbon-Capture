import serial                                               #import pyserial library
import numpy                                                #import numpy
import matplotlib.pyplot as plt                             #import matplotlib library
from drawnow import *                                       #import drawnow library
import time                                                 #import time library
import matplotlib.animation as animation

temp = []                                                   #temperature array
hum = []                                                    #humidity array
arduinoData = serial.Serial('com3', 9600)                   #creating serial object name arduinoData
plt.ion()                                                   #Tell matplotlib user wants interactive mode to plot live data
cnt = 0                                                     #counter 


def makeFig():                                              #create a function that makes the plot
    plt.ylim(32,122)                                        #limit for left y axis 
    plt.title('Temperature & Humidity vs Time')             #gives title to the graph
    plt.grid(True)                                          #gives grid to the graph    
    plt.ylabel('Temperature (F)')                           #gives label to left y axis 
    plt.xlabel('Time (s)')                                  #gives label to the x axis
    plt.plot(temp, 'ro-', label='Temperature')              #plots the temp, gives it a red line and circle for 'dots', and legend label
    plt.legend(loc='lower left')                            #puts the legend for temperature on the lower left
    plt2 = plt.twinx()                                      #using the same plot, but on the right side. Creating a righty axis
    plt.ylim(0,100)                                         #limit for the right y axi
    plt2.plot(hum, 'b^-', label='hum')                      #plot the humidity, gives it a blue line and triangle 'dots', and legend label
    plt2.set_ylabel('Humidity %')                           #gives label to the right y axis
    plt2.legend(loc='lower right')                          #puts the legend of the humidity on the lower right 
    

while True:                                                 #while loop that loops forever
    while (arduinoData.inWaiting() == 0):                   #wait here until there is data
        pass                                                #do nothing
    arduinoString = arduinoData.readline().decode('utf-8').strip() #convert data into a string
    dataArray = arduinoString.split(',')                    #data as an array, split the string at the comma 
    T = float(dataArray[0])                                 #convert first element to a floating number
    H = float(dataArray[1])                                 #convert second element to a floating number
    temp.append(T)                                          #build temp array by appending T readings
    hum.append(H)                                           #build hum array by appendig H readings
    drawnow(makeFig)                                        #call drawnow to update our live graph
    plt.pause(.000001)                                      #a small pause 
    cnt = cnt + 1                                           #adds one to the counter called earlier
    if (cnt > 30):                                          #after enough additions, if the counter is above 30
        temp.pop(0)                                         #pop out the number at the 0 label and effectively 
        hum.pop(0)                                          #move the graph to the left, keeping the graph neat
    
