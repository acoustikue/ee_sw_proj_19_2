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


import os, sys, socket
from flask import Flask, render_template, url_for, send_from_directory, request

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(
            os.path.dirname(
                os.path.abspath(os.path.dirname(__file__))) )))

# user 
import config as cf
from loggingd import *

# Flask app
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
	
	return 'index'	
	
if __name__ == '__main__':
	
    #print(socket.gethostbyname(socket.getfqdn()))
    
    app.run(debug=False, host='0.0.0.0')





