#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

LED = [26,27,22,18,13]
SWITCH = [17,5]
DELAY = 0.5
INTERRUPT = False

def setup():
        GPIO.setmode(GPIO.BCM)       
        GPIO.setwarnings(False)       
        GPIO.setup(LED[0], GPIO.OUT, initial = False)
        GPIO.setup(LED[1], GPIO.OUT, initial = True)
        GPIO.setup(LED[2], GPIO.OUT, initial = True)
        GPIO.setup(LED[3], GPIO.OUT, initial = False)
        GPIO.setup(LED[4], GPIO.OUT, initial = True)
        GPIO.setup(SWITCH[0], GPIO.IN)
        GPIO.setup(SWITCH[1], GPIO.IN)

def destroy():
    GPIO.cleanup()                      
    sys.exit()

def loop():
        global INTERRUPT
        GPIO.add_event_detect(SWITCH[1], GPIO.FALLING, callback = walker, bouncetime = 500)
        while True:
                input_value = GPIO.input(SWITCH[0])
                GPIO.output(LED[0], False)
                GPIO.output(LED[1], True)
                GPIO.output(LED[2], True)
                GPIO.output(LED[3], False)
                GPIO.output(LED[4], True)
                GPIO.wait_for_edge(SWITCH[0], GPIO.RISING)
                GPIO.output(LED[0], False)
                GPIO.output(LED[1], False)
                GPIO.output(LED[2], True)
                time.sleep(3)
                if INTERRUPT == True:
                        INTERRUPT = False
                        continue
                GPIO.output(LED[0], True)
                GPIO.output(LED[1], True)
                GPIO.output(LED[2], False)
                time.sleep(15)
                if INTERRUPT == True:
                        INTERRUPT = False
                        continue
                GPIO.output(LED[0], True)
                GPIO.output(LED[1], False)
                GPIO.output(LED[2], True)
                time.sleep(3)
                if INTERRUPT == True:
                        INTERRUPT = False
                        continue

def walker(channel):
        global INTERRUPT
        INTERRUPT = True
        time.sleep(1)
        GPIO.output(LED[0], True)
        GPIO.output(LED[1], False)
        GPIO.output(LED[2], True)
        time.sleep(3)
        GPIO.output(LED[0], False)
        GPIO.output(LED[1], True)
        GPIO.output(LED[2], True)
        time.sleep(1)
        GPIO.output(LED[3], True)
        GPIO.output(LED[4], False)
        time.sleep(10)
        GPIO.output(LED[3], False)
        GPIO.output(LED[4], True)

        
        
if __name__ == '__main__':
    global INTERRUPT
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        while True:
            loop()
    except KeyboardInterrupt:  
        destroy()

