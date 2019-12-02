# [Basic EE Ex SW Project] Electronic Engineering Software Project 19-2(xix_ii)
# 0.0.0va, 19.08.21. First tested, last update 19.11.28.
# written by acoustikue(SukJoon Oh)
#
#    ____     __      __                 ____  __ 
#   / __/_ __/ /____ / /__  ___  ___    / __ \/ / 
#  _\ \/ // /  '_/ // / _ \/ _ \/ _ \  / /_/ / _ \
# /___/\_,_/_/\_\\___/\___/\___/_//_/  \____/_//_/
#                                                     
# Visual Studio 2017 Professional Blank Python Project
# rpi_sim.py
# 
#
# http://tieske.github.io/rpi-gpio/modules/GPIO.html
# https://gpiozero.readthedocs.io/en/stable/
#

import os, sys

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# user 
import config as cf
from loggingd import *

# Use this script only in Windows environment!!
loggerd.new() # always start new logs,
# since this is a test!!
           
# This is a simple simulator for console environment in Windows.
# made by SukJoon Oh, 2019 Nov.

# utility
def printNlog(str):
    print('\t' + str)
    loggerd.log(str)


class GPIOSim:
    def __init__(self):
        self.OUT = 'GPIO.OUT'
        self.IN = 'GPIO.IN'
        self.BCM = 'GPIO.BCM'

    def setmode(self, mode):
        console_str = '[GPIOSim] SETMODE: {mode}'.format(mode=mode)
        printNlog(console_str)

    def setup(self, pin, mode):
        console_str = '[GPIOSim] SETUP: pin{pin} to {mode}'.format(pin=pin, mode=mode)
        printNlog(console_str)

    def output(self, pin, out):
        console_str = '[GPIOSim] OUT: pin{pin} to {mode}'.format(pin=pin, out=out)
        printNlog(console_str)

    def cleanup(self):
        console_str = '[GPIOSim] CLEANUP'
        printNlog(console_str)


class MotionSensorSim:
    def __init__(self):
        pass


class Adafriuit_DHTSim:
    def __init__(self):
        self.DHT11 = 'DHT11'

    def read_retry(self, sensor, pin):
        return 'sample value {temp, humid}'
    

# Global
GPIO = GPIOSim()


