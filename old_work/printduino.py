import numpy
import matplotlib.pyplot as plt
from drawnow import *
from datetime import datetime

temp = []
hum = []
co = []
no2 = []
small = []
big = []
start_time = datetime.now()
    
def makeFig():                                              #create a function that makes the plot
    plt.title('Humidity % vs Time')
    plt.grid(True)
    plt.ylim(0,100)
    plt.ylabel('Humidity %')
    plt.xlabel('Time (s)')
    plt.plot(hum, 'b-')
def makeFig2():
    figure(1)
    plt.title('Temperature (F) vs Time')
    plt.grid(True)
    plt.ylim(32,122)
    plt.ylabel('Temperature (F)')
    plt.xlabel('Time (s)')
    plt.plot(temp,'r-')
def makeFig3():
    figure(2)
    plt.title('Carbon Monoxide vs Time')                    #creating all of the graphs 
    plt.grid(True)
    plt.ylim(0,100)
    plt.ylabel('CO (PPM)')
    plt.xlabel('Time(s)')
    plt.plot(co,'g-')
def makeFig4():
    figure(3)
    plt.title('Small PM and Large PM vs Time')
    plt.grid(True)
    plt.ylim(0,20)
    plt.ylabel('small PM2.5 (PPM)')
    plt.xlabel('Time (s)')
    plt.plot(small,'y-')
def makeFig5():
    figure(4)
    plt.title("Large PM vs Time")
    plt.grid(True)
    plt.ylim(0,20)
    plt.ylabel('Large PM10 (PPM)')
    plt.xlabel('Time (s)')
    plt.plot(big,'g-')
def makeFig6():
    figure(5)
    plt.title("Nitrogen Dioxide Levels vs Time")
    plt.grid(True)
    plt.ylim(0,300)
    plt.ylabel('NO2 (PPB)')
    plt.xlabel('Time (s)')
    plt.plot(no2,'k-')

while True:
    prompt_start = print("Which type of data do you want to view?")
    try:
        prompt_input = int(input("[1]Temperature \n[2]Humidity \n[3]Carbon Monoxide \n[4]Small PM \n[5]Large PM \n[6]Nitrogren Dioxide \n[0]End Program \nEnter a number (0-6): "))
        if prompt_input == 1:
            drawnow(makeFig2)
            print("Current Temperature")
        elif prompt_input == 2:
            drawnow(makeFig)
            print("Current Humidity")
        elif prompt_input == 3:
            drawnow(makeFig3)
            print("CO Currently")
        elif prompt_input == 4:
            drawnow(makeFig4)
            print("Small PM")
        elif prompt_input == 5:
            drawnow(makeFig5)
            print("Large PM")
        elif prompt_input == 6:
            drawnow(makeFig6)
            print("Nitrogen Dioxide")
        elif prompt_input == 0:
            print("Goodbye!")
            break
        else:
            print("Enter a valid number (1-6)")
    except ValueError:
        print("This is not a number")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print()
            
