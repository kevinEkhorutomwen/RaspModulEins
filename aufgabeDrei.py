#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

LED_1 = 26
LED_2 = 27
LED_3 = 22
SWITCH_1 = 17
DELAY = 0.5




def setup():
        GPIO.setmode(GPIO.BCM)       
        GPIO.setwarnings(False)       
        GPIO.setup(LED_1, GPIO.OUT)
        GPIO.setup(LED_2, GPIO.OUT)
        GPIO.setup(LED_3, GPIO.OUT)
        GPIO.setup(SWITCH_1, GPIO.IN)   

def destroy():
    GPIO.cleanup()                      
    sys.exit()

def loop():
        while True:
                input_value = GPIO.input(SWITCH_1)
                GPIO.output(LED_1, False)
                GPIO.output(LED_2, True)
                GPIO.output(LED_3, True)
                GPIO.wait_for_edge(SWITCH_1, GPIO.RISING)
                GPIO.output(LED_1, False)
                GPIO.output(LED_2, False)
                GPIO.output(LED_3, True)
                time.sleep(3)
                GPIO.output(LED_1, True)
                GPIO.output(LED_2, True)
                GPIO.output(LED_3, False)
                time.sleep(15)
                GPIO.output(LED_1, True)
                GPIO.output(LED_2, False)
                GPIO.output(LED_3, True)
                time.sleep(3)
                        
        
if __name__ == '__main__':  
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()
