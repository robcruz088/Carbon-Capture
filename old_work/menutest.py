import numpy
import matplotlib.pyplot as plt
from drawnow import *
from datetime import datetime

temp = []                                                   #temperature array
hum = []                                                    #humidity array
co = []                                                     #carbon monoxide array
no2 = []                                                     #nitrogen dioxide array 
small = []                                                  #small Particulate Matter array
big = []                                                    #large particulate matter array
cnt = 0                                                     #counter starter
start_time = datetime.now()
end_time = datetime.now()

print("Welcome to the Pollution Detection System!\nChoose one of the following options")
selector = int(input("[1]Humidity\n[2]Temperature\n[3]Carbon Monoxide\n[4]Small/Large Particulate Matter\n[5]Nitrogen Dioxide\n[0]Finished\n"))

def makeFig1():                                              
    figure()
    plt.title('Humidity % vs Time')
    plt.grid(True)
    plt.ylim(0,100)
    plt.ylabel('Humidity %')
    plt.xlabel('Time (s)')
    plt.plot(hum, 'b-')
def makeFig2():
    figure()
    plt.title('Temperature (F) vs Time')
    plt.grid(True)
    plt.ylim(32,122)
    plt.ylabel('Temperature (F)')
    plt.xlabel('Time (s)')
    plt.plot(temp,'r-')
def makeFig3():
    figure()
    plt.title('Carbon Monoxide vs Time')                    #creating all of the graphs 
    plt.grid(True)
    plt.ylim(0,100)
    plt.ylabel('CO (PPM)')
    plt.xlabel('Time(s)')
    plt.plot(co,'g-')
def makeFig4():
    figure()
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
def makeFig5():
    figure(5)
    plt.title("Nitrogen Dioxide Levels vs Time")
    plt.grid(True)
    plt.ylim(0,300)
    plt.ylabel('NO2 (PPB)')
    plt.xlabel('Time (s)')
    plt.plot(no2,'k-')
    
try:
    if selector == 1:
        makeFig1()
    elif selector == 2:
        makeFig2()
    elif selector == 3:
        makeFig3()
    elif selector == 4:
        makeFig4()
    elif selector == 5:
        makeFig5()
    elif selector == 0:
        print("You ran the program for ".format(end_time - start_time))
        print("Goodbye!")
    else:
        print("Please select a valid number")

except ValueError:
    print("Can only input 1-5 and 0. Please enter the correct input")
    











    




