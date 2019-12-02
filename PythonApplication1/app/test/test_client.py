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


# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# user 
import config as cf
from loggingd import *

from ctrl.socket_pi import SocketPi



#
# Client class        
class SocketPiClient(SocketPi):

    def __init__(self):
        print('\t[SocketPiClient] Initiated.')
        loggerd.log('Initiated', 'client')

        # self.do_connect_action = None

        super(__class__, self).__init__('client')

    #
    # overloading
    def _make_socket(self):
        if not self._isValid('client'): return False

        print('\t[SocketPiClient] Make socket for client.')
        loggerd.log('Making socket.', 'client')

        self.socket \
            = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.socket.bind((cf.SERVER_NAME, 0))

        # This function returns handle
        return self.socket


    # interface
    def doStartConnect(self, action):

        try:
            # create socket
            handle = self._make_socket()

            self.socket.connect((cf.SERVER_NAME, cf.SERVER_PORT))

            # do work here.
            action(self.socket)

            

        except Exception as e:
            print('\t[SocketPiClient] do_connect exception catched.')
            loggerd.log('do_connect exception.', 'client')

            print('\t' + str(e))
            loggerd.log(str(e), 'server')

        finally:
            self.socket.close()
        
            
    # 
    # Registered function mush have a parameter.
    # socket!!






if __name__ == '__main__':
    
    loggerd.new()

    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    client = SocketPiClient()

    def action(socket):
        print('\t[action]')

        msg = input()

        socket.send(msg.encode('utf-8'))
    while(1):
        client.doStartConnect(action)

    pass