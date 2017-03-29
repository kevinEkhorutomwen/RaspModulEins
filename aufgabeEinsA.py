#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

LED_1 = 26
LED_2 = 27
LED_3 = 22
SWITCH_1 = 17
SWITCH_2 = 5
SWITCH_3 = 13
SWITCH_4 = 19

def setup():
        GPIO.setmode(GPIO.BCM)       
        GPIO.setwarnings(False)       
        GPIO.setup(LED_1, GPIO.OUT)
        GPIO.setup(LED_2, GPIO.OUT)
        GPIO.setup(LED_3, GPIO.OUT)
        GPIO.setup(SWITCH_1, GPIO.IN)
        GPIO.setup(SWITCH_2, GPIO.IN)
        GPIO.setup(SWITCH_3, GPIO.IN)
        GPIO.setup(SWITCH_4, GPIO.IN) 

def destroy():
    GPIO.cleanup()                      
    sys.exit()

def loop():
        while True:
                input_value_eins = GPIO.input(SWITCH_1)
                input_value_zwei = GPIO.input(SWITCH_2)
                input_value_drei = GPIO.input(SWITCH_3)
                input_value_vier = GPIO.input(SWITCH_4)
                
                if input_value_eins == True:
                        GPIO.output(LED_1, False)
                if input_value_zwei == True:
                        GPIO.output(LED_2, False)
                if input_value_drei == True:
                        GPIO.output(LED_3, False)
                if input_value_vier == True:
                        GPIO.output(LED_1, True)
                        GPIO.output(LED_2, True)
                        GPIO.output(LED_3, True)
                          


        
if __name__ == '__main__':  
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()
