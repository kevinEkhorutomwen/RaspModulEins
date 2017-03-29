#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

LED_1 = 26
SWITCH_1 = 17




def setup():
        GPIO.setmode(GPIO.BCM)       
        GPIO.setwarnings(False)       
        GPIO.setup(LED_1, GPIO.OUT)
        GPIO.setup(SWITCH_1, GPIO.IN)   

def destroy():
    GPIO.cleanup()                      
    sys.exit()

def loop():
        onOff = False
        check = False
        while True:
                input_value = GPIO.input(SWITCH_1)                
                if input_value == True:
                        if check == False:
                                if onOff == False:
                                        onOff = True
                                else:
                                        onOff = False
                                check = True
                else:
                        check = False
                GPIO.output(LED_1, onOff)
                time.sleep(0.1)
        
if __name__ == '__main__':  
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()
