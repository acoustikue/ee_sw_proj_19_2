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
# test_server.py
# 
#
# http://tieske.github.io/rpi-gpio/modules/GPIO.html
# https://gpiozero.readthedocs.io/en/stable/
#


import os, sys
import time

import socket
import socketserver

import threading

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# user 
import config as cf
from loggingd import *

# This is a socket wrapper for RPI.
# Test has been partially done in Windows environment,
# but I guess it will work fine on Linux also.

# SocketPi Wrapper class, 
# Author: SukJoon Oh, 2019 Nov.
class SocketPi:
    def __init__(self, mode=''):

        self.mode = ''
        self.socket = None

        if mode.lower() == 'server': 
            self.mode = 'server'
            loggerd.log('Server mode.')

        elif mode.lower() == 'client': 
            self.mode = 'client'
            loggerd.log('Client mode.')

        elif mode == '':
            if cf.DEBUG_FLAG == True:
                print('\tUnable to identify operating mode.')
            loggerd.log('Unable to identify operating mode.')

        # Automatically makes socket if operating mode is known.

    # 
    def _isValid(self, mode):
        if mode != self.mode:

            print('\tNot a valid function in this mode.')
            loggerd.log('Not a valid function in this mode.')
            return False

        else: return True

    # close socket
    # make sure you have opened socket before using this function!!
    def _close_socket(self):
        self.socket.close()




