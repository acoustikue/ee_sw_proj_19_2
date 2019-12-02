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
# config.py
# 
# Vers 1, selenium type
# 08.22. Seems unnecessary. 
# from selenium import webdriver
#
# Following library needed, 
# pyfcm, flask
# prefix?
#
# This project is also designed for running consistently on raspberry-pi, 
# a small scale home server.
# But it will also work on any other linux-based OS.

import os
import platform
import copy

LOG_ENABLE = True
DEBUG_FLAG = True
RUNTIME = ''

# Socket
# Hard coded
SERVER_PORT = 8888
SERVER_NAME = '192.168.0.42'
BUFFER_SIZE = 1024


# is on Windows?

# 
# information
PROJECT_CODE = 'rpi'
PROJECT_OS = 'Windows'
PROJECT_SYS = ''
PROJECT_VERSION = '0.0.0va'

CURRENT_CODE = 'wnd'
CURRENT_OS = str(platform.system())
CURRENT_SYS = CURRENT_OS + ' ' + str(platform.release()) + ' ' + str(platform.version())

# Logging settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FCM_DIR = ''

DIR_IDENTIFIER = ''

LOG_DIR = ''
LOG_FILENAME_PREFIX = 'log-'

if CURRENT_OS == 'Windows':
    FCM_DIR = BASE_DIR + '\\data\\'
elif CURRENT_OS == 'Linux': 
    FCM_DIR = BASE_DIR + '/data/'

FCM_SERVER_FILE = FCM_DIR + 'server_fcm.data'
FCM_DEVICE_FILE = FCM_DIR + 'device_fcm.data'

if CURRENT_OS == 'Windows':
    LOG_DIR = BASE_DIR + '\\logs\\'
    RUNTIME = 'na'

    # MESSAGE_DIR = BASE_DIR + '\\fcm_message\\'
elif CURRENT_OS == 'Linux': 
    LOG_DIR = BASE_DIR + '/logs/'
    RUNTIME = 'rpi'
    # MESSAGE_DIR = BASE_DIR + '/fcm_message/'


# First!!
# Make directory if there is no log folder
if not(os.path.isdir(LOG_DIR)): os.makedirs(os.path.join(LOG_DIR))
if not(os.path.isdir(FCM_DIR)): os.makedirs(os.path.join(FCM_DIR))

if not(os.path.isfile(FCM_SERVER_FILE)):
    with open(FCM_SERVER_FILE, "w", encoding="utf-8") as file:
        pass

if not(os.path.isfile(FCM_DEVICE_FILE)):
    with open(FCM_DEVICE_FILE, "w", encoding="utf-8") as file:
        pass
# if not(os.path.isdir(MESSAGE_DIR)): os.makedirs(os.path.join(MESSAGE_DIR))

PROJECT_BANNER = '[EE19_2] ' + PROJECT_CODE + ', ' + PROJECT_VERSION
PROJECT_BANNER += (', ' + CURRENT_SYS + '\n\tCopyright (C) 2019 SukJoon Oh')



# Rpi setting flags
RPI_GPIO_ENABLE = False

if CURRENT_OS == 'Windows':
    pass

elif CURRENT_OS == 'Linux': 
    RPI_GPIO_ENABLE = False


# Rpi GPIO settings





# Scripts
# platform

# Make sure to print only necessary information, for simple logs.
# print(PROJECT_BANNER)


# 
# Parameter: -
# Returns: -
# Author: SukJoon Oh
def showConfig():

    #if KENS_ENABLE is True:
    #    print('\tKENS_ENABLE(1). KENS module will be loaded.')

    print('config:')

    print('\tPROJECT_CODE   \t' + PROJECT_CODE)
    print('\tPROJECT_OS     \t' + PROJECT_OS)
    print('\tPROJECT_SYS    \t' + PROJECT_SYS)
    print('\tPROJECT_SYS    \t' + PROJECT_SYS)
    print('\tPROJECT_VERSION\t' + PROJECT_VERSION)

    print('\tCURRENT_CODE   \t' + CURRENT_CODE)
    print('\tCURRENT_OS     \t' + CURRENT_OS)
    print('\tCURRENT_SYS    \t' + CURRENT_SYS)

    print('\tBASE_DIR       \t' + BASE_DIR)
    print('\tLOG_PREFIX     \t' + LOG_FILENAME_PREFIX)

    print('\tRPI_GPIO_ENABLE\t' + str(RPI_GPIO_ENABLE))

# Executing this script?
if __name__ == '__main__':

    # First print banner
    print(PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    # Show configuration variables
    showConfig()





