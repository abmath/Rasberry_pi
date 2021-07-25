# Starting code to measure CPU temperature for 10 seconds and output in a text file

# Import libraries
import time # For time delay
import datetime
from gpiozero import CPUTemperature # To fetch CPU temperature

myfile = open('temperatures.txt','w')
for i in range(0,10):
    temp = CPUTemperature()
    ts = datetime.datetime.now()
    #print(temp)
    line = str(ts)+' '+str(temp)
    print(line)
    myfile.write(line)
    time.sleep(1)
    
myfile.close()
