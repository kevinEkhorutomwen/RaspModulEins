#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

LED_1 = 20
DELAY = 1

def setup():
        GPIO.setmode(GPIO.BCM)       
        GPIO.setwarnings(False)       
        GPIO.setup(LED_1, GPIO.OUT)   

def destroy():
    GPIO.cleanup()                      
    sys.exit()

def loop():
        while True:
                GPIO.output(LED_1,False)
                time.sleep(DELAY)
                GPIO.output(LED_1,True)
                time.sleep(DELAY)

if __name__ == '__main__':  
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()
