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
import copy
import socket

# Necessary
from pyfcm import FCMNotification


# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# user 
import config as cf
from loggingd import *

# FcmPi class
# This object is used to set registered device information
class FcmPi:

    def __init__(self): 

        # Here holds essential information, 
        # Firebase server key and device token.
        self._server_key = ''
        self._device_token = []

        with open(cf.FCM_SERVER_FILE, "r", encoding="utf-8") as file:
            self._server_key = file.readline()

        with open(cf.FCM_DEVICE_FILE, "r", encoding="utf-8") as device_file: # Read file.

            list = device_file.readlines() # Read api key

            # if there are multiple keys, then something is wrong.
            if len(list) is 0: 
                print('\tNo device token found.')

            else:
                # print('\tServer API key found.')
                for user in list:
                    self._device_token.append(str(user).rstrip('\n')) # Remove \n 
        
        #
        # Server
        self.fcm_service = FCMNotification(api_key=self._server_key)


    # Parameter: String, String, Action(String, mostly URL)
    # Returns: -
    # Author: acoustikue(SukJoon Oh)
    def notifyMultipleDevice(self, m_title, m_body, action='', kwargs=None):

        print('Push:')

        for token in self._device_token:
            print('\t' + token[0:19] + '...')
        # send push!
        self.fcm_service.notify_multiple_devices(registration_ids=self._device_token, \
                                                 message_title=m_title, message_body=m_body, click_action=action \
                                                     , extra_notification_kwargs=kwargs)

    pass

fcm_server = FcmPi()



if __name__ == '__main__':
    
    loggerd.new()

    from ctrl.provider import app

    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    fcm_server = FcmPi()

    #fcm_server.notifyMultipleDevice('Test', 'Test', '', {'image': 'https://i.ytimg.com/vi/sioEY4tWmLI/maxresdefault.jpg'})
    #fcm_server.notifyMultipleDevice('Test', 'Test', '', {'image': ''})
    fcm_server.notifyMultipleDevice('Test', 'Test', 'http://' + str( socket.gethostbyname(socket.getfqdn()) + ':5000/static/python.png'), \
        {'image': 'http://' + str( socket.gethostbyname(socket.getfqdn()) + ':5000/static/python.png')})





    input()

    pass















