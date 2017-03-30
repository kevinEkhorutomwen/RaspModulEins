#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

SWITCH = [17,27,22]
DELAY = 0.5
PKW, LKW = 0, 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SWITCH[0], GPIO.IN)
    GPIO.setup(SWITCH[1], GPIO.IN)
    GPIO.setup(SWITCH[2], GPIO.IN)

def destroy():
    GPIO.cleanup()
    sys.exit()

def loop():
    GPIO.add_event_detect(SWITCH[0], GPIO.FALLING, callback = countPKW, bouncetime = 200)
    GPIO.add_event_detect(SWITCH[1], GPIO.FALLING, callback = countLKW, bouncetime = 200)
    while True:
        GPIO.wait_for_edge(SWITCH[2], GPIO.RISING)
        output()
        destroy()

def countPKW(channel):
    global PKW
    PKW = PKW + 1
    output()

def countLKW(channel):
    global LKW
    LKW = LKW +1
    output()

def output():
    global PKW
    global LKW
    print(chr(27) + "[2J")
    print 'Anzahl der PKWs: ' + str(PKW)
    print 'Anzahl der LKWs: ' + str(LKW)



if __name__ == '__main__':
    global INTERRUPT
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
            loop()
    except KeyboardInterrupt:
        destroy()

