#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys
import os

LED = [17,27,22]
status = os.statvfs(´/´)
s = os.statvfs


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED[0], GPIO.OUT)
    GPIO.setup(LED[1], GPIO.OUT)
    GPIO.setup(LED[2], GPIO.OUT)

def destroy():
    GPIO.cleanup()
    sys.exit()

def loop():
    while True:
        MB = status.f_bsize * s.f_bavail / 1048576
        print MB

def output():

if __name__ == '__main__':
    global INTERRUPT
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

