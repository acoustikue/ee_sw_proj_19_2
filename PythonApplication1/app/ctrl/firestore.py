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
# firestore.py
# 
# pip install google-cloud-storage
# pip install firebase
# pip install firebase-admin
#
# http://tieske.github.io/rpi-gpio/modules/GPIO.html
# https://gpiozero.readthedocs.io/en/stable/
#

import os, sys
import copy

from datetime import datetime, timedelta

# Necessary
#from google.cloud import storage
#from firebase import firebase

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

# user 
import config as cf
from loggingd import *

# gs://ee-sw-proj-19-2.appspot.com






if __name__ == '__main__':
    
    loggerd.new()

    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    from google.cloud import storage
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cf.FIRESTORE_ADMIN_FILE
    

    client = storage.Client()
    bucket = client.get_bucket('ee-sw-proj-19-2.appspot.com')

    imageBlob = bucket.blob("sample.png")
    imageBlob.upload_from_filename(cf.FCM_DIR + 'python.png')

    print(imageBlob.generate_signed_url(expiration=timedelta(hours=1), method='GET'))

    input()

    pass

