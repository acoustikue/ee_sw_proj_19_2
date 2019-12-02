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

# 
# 
class Command:
    
    def __init__(self):

        # Dictionary
        self.command_dictionary = {}
        
        print('\tCommand dictionary loaded')
        loggerd.log('Dictionary loaded.', 'comm')


    # Parameter: String, Callback
    # Returns: -
    # Author: acoustikue(SukJoon Oh)
    def registerCommand(self, command, callback):
        self.command_dictionary[command] = callback
    
    # Parameter: String
    # Returns: -
    # Author: acoustikue(SukJoon Oh)
    def unregisterCommand(self, command):
        self.command_dictionary.popitem(command)

    
        # inner
    def _isValid(self, command):
        
        if self.command_dictionary.get(command) == None:
            return False

        else: return True


    def call(self, command):

        if self._isValid(command):
            return self.command_dictionary[command]()

        else: return None


# Global
command_handle = Command()



if __name__ == "__main__":

    # 
    # 
    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    def help():
        print('\tHelp called.')

    command_handle.registerCommand('help', help)

    command_handle.call('help')










