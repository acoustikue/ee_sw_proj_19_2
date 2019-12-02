# [Basic EE Ex SW Project] Electronic Engineering Software Project 19-2(xix_ii)
# 0.0.0va, 19.08.21. First tested, last update 19.08.23.
# written by acoustikue(SukJoon Oh)
#
#    ____     __      __                 ____  __ 
#   / __/_ __/ /____ / /__  ___  ___    / __ \/ / 
#  _\ \/ // /  '_/ // / _ \/ _ \/ _ \  / /_/ / _ \
# /___/\_,_/_/\_\\___/\___/\___/_//_/  \____/_//_/
#                                                     
# Visual Studio 2017 Professional Blank Python Project
# test_gpio.py
# 
#
# http://tieske.github.io/rpi-gpio/modules/GPIO.html
# https://gpiozero.readthedocs.io/en/stable/
#

import os, sys
import time

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# user 
import config as cf
from loggingd import *



# Start
if cf.RUNTIME == 'rpi':

    import RPI.GPIO as GPIO

    if cf.DEBUG_FLAG:
        if cf.LOG_ENABLE: print('!!!\tLog enabled.')
        pass

    # Do something here with hw control code.

    pass

elif cf.RUNTIME == 'na': # Windows
    if cf.DEBUG_FLAG:
        if cf.LOG_ENABLE: print('!!!\tLog enabled.')

    from rpi_sim import *

else:
    pass


# test
if __name__ == '__main__':

    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    if cf.RUNTIME == 'na': # Windows
    GPIO.setmode(GPIO.BCM)
    
    time.sleep(1)
    GPIO.setup(23, GPIO.OUT)

    GPIO.cleanup()