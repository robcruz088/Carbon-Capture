import serial
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
arduinoData = serial.Serial('com3',9600)
plt.ion()
cnt = 0
start_time = datetime.now()

plt.rcParams['savefig.facecolor'] = "0.8"

def subplot(ax, fontsize = 12):
    ax.plot([1,50])

    ax.locator_params(nbins=3)
    ax.set_xlabel('Time (s)', fontsize = fontsize)
    ax.set_ylabel('y-label', fontsize = fontsize)
    ax.set_title('Title', fontsize = fontsize)
    gridplot.on()

plt.close('all')

def makeFig():
    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2, sharey = False)
    subplot(ax1)
    ax1.set_title('Temperature')
    ax1.set_ylabel('Temperature (F)')
    ax1.set_ylim([32,122])
    subplot(ax2)
    ax2.set_title('Humidity')
    ax2.set_ylabel('Humidity %')
    ax2.set_ylim([0,100])
    subplot(ax3)
    ax3.set_title('Carbon Monoxide')
    ax3.set_ylabel('CO (PPM)')
    ax3.set_ylim([1,20])
    subplot(ax4)
    ax4.set_title('Nitrogren Dioxide')
    ax4.set_ylabel('NO2 (PPB)')
    ax4.set_ylim([1,20])
    plt.tight_layout(pad = 0.4, w_pad = 0.5, h_pad = 1.0)

