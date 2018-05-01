from gpiozero import InputDevice, OutputDevice, LED
from time import sleep, time
import os
import random
from datetime import datetime

trig = OutputDevice(4)
echo = InputDevice(17)
message = LED(22)
Sec = 1

sleep(2)

def robot(text):
    os.system("pico2wave -w hello.wav ' " + text + " ' && aplay hello.wav")

def get_pulse_time():
    trig.on()
    sleep(0.00001)
    trig.off()
    
    while echo.is_active == False:
        pulse_start = time()

    while echo.is_active == True:
        pulse_end = time()

    sleep(0.06)

    try:
        return pulse_end - pulse_start
    except:
        return 0.02

def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2
    return distance
now = datetime.now()    
print("Waiting for Visitor @ %s" % now)


time_1=2.3
time_2=2.3
time_3=2.3
x=0
y=0
while True:
    duration = get_pulse_time()
    distance = calculate_distance(duration)
    time_1 = distance
    print("time_1 ",distance)
    x = time_1 - time_2
    if (x**2)**.5 > .2:     ## If distance is noticably different from the last reading, start this loop.
        sleep(.2)
        duration = get_pulse_time()
        distance = calculate_distance(duration)
        time_3 = distance   ## Get another distance reading
        print("time_3 ",distance)
        y = time_3 - time_2 
        if ((y)**2)**.5 > .2:           ## Compare this 2nd reading to the one when there was no motion / no one coming or going.
            if time_3 - time_1 >= .2:   ## If this 2nd reading is getting farther away, run goodbye script.
                print("Goodbye")
                message.on()
                robot("Goodbye")
                sleep(5)
                message.off()
                time_1=time_2
                time_3=time_2             
            elif time_1-time_3 >= .2:   ## If this 2nd reading is getting closer, run the hello script.
                message.on()
                print("Hello")
                robot("Hello, Welcome to the CITE lab")
                sleep(5)
                message.off()
                time_1=time_2
                time_3=time_2          
            else:                       ## Otherwise no one is coming or going, and restart the loop.
                sleep(.2)
        else:
            sleep(.2)
    else:
        time_2 = time_1
        sleep(.2)
    

                                
    
