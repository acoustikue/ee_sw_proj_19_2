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
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cf.FIRESTORE_ADMIN_FILE

# FirestorePi class
# This class provides access to Firebase storage.
# Author: SukJoon Oh
class FirestorePi:

    #
    # ctor
    def __init__(self):
        try:
            self.client = storage.Client()
            self.bucket = self.client.get_bucket(cf.FIRESTORE_BUCKET)

        except Exception as e:
            print('\t[Firestore] ' + e)
            loggerd.log(e, 'fs')

    #
    # Target image must be in the predefined area.
    # The area(folder) is defined in config.py
    def uploadImage(self, target=''):

        # file name which will be stored
        imageBlob = self.bucket.blob(target)
        imageBlob.upload_from_filename(cf.FIRESTORE_UPLOAD_DIR + target) # upload!

        print('\tFile successfully uploaded.')
        loggerd.log('File upload complete.', 'fs')

        return imageBlob.generate_signed_url(expiration=timedelta(hours=1), method='GET')


# Global
firestore_handle = FirestorePi()



if __name__ == '__main__':
    
    loggerd.new()

    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    # This is how you use the object
    url = firestore_handle.uploadImage('python.png')
    
    # Lets use the FCM server.
    from fcm import fcm_server
    fcm_server.notifyMultipleDevice('AlertPi 작동 감지',\
        '움직임이 감지되었습니다. 확인하십시오.',\
        url, {'image': url})


    input()

    pass

