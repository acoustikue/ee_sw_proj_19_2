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





#
# Server class
class SocketPiServer(SocketPi):
    
    def __init__(self):
        print('\t[SocketPiServer] Initiated.')
        loggerd.log('Initiated', 'server')

        super(__class__, self).__init__('server')

    #
    # overloading
    def _make_socket(self):
        print('\t[SocketPiServer] _make_socket')
        loggerd.log('_make_socket', 'server')

        self.socket \
            = socketserver.TCPServer((cf.SERVER_NAME, cf.SERVER_PORT), \
                                     SocketPiServer_TCPHandler)
        
        # This function returns handle
        return self.socket


    def doStart(self):
        try:
            print('\t[SocketPiServer] Listening...')
            loggerd.log('Listening...', 'server')
            
            # create socket
            handle = self._make_socket()

        except Exception as e:
            print('\t[SocketPiServer] do_listen exception catched.')
            loggerd.log('do_listen exception.', 'server')

            print('\t' + str(e))
            loggerd.log(str(e), 'server')

        return handle


    def doListen(self):
        try:           
            self.socket.serve_forever()

        except Exception as e:
            print('\t[SocketPiServer] do_listen exception catched.')
            loggerd.log('do_listen exception.', 'server')

            print('\t' + str(e))
            loggerd.log(str(e), 'server')

        finally:
            pass



    # interface
    def doStartListen(self):

        try:
            print('\t[SocketPiServer] Listening...')
            loggerd.log('Listening...', 'server')
            
            # create socket
            handle = self._make_socket()
            # do work here.

            self.socket.serve_forever()

        except Exception as e:
            print('\t[SocketPiServer] do_listen exception catched.')
            loggerd.log('do_listen exception.', 'server')

            print('\t' + str(e))
            loggerd.log(str(e), 'server')

        finally:
            pass

    # 
    # 
    def doListenDaemon(self):

        notify_thread = threading.Thread(target=self._daemonWatchdog)
        notify_thread.daemon = True 
        notify_thread.start()

        # self._daemonWatchdog()

    def _daemonWatchdog(self):

        server_thread = threading.Thread(target=server.doListen)
        server_thread.daemon = True 
        server_thread.start()

        while(1):
            print('\t[Daemon] Daemon watchdog running. {name} alive: {stat}'.format( \
                name=server_thread.getName(), stat=server_thread.isAlive()))
            time.sleep(5)

            

        
        

    #
    # Multi client management
    def _m_client_handler(self, client_sock, addr):
        pass


    
# Server thread run
def run_server_background():

    # make socket for server
    server = SocketPiServer()
    server.do_listen()

    pass


#
# Client class        
class SocketPiClient(SocketPi):

    def __init__(self):
        print('\t[SocketPiClient] Initiated.')
        loggerd.log('Initiated', 'client')

        self.do_connect_action = None

        super(__class__, self).__init__('client')

    #
    # overloading
    def _make_socket(self):
        if not self._isValid('client'): return False

        print('\t[SocketPiClient] Make socket for client.')
        loggerd.log('Making socket.', 'client')

        self.socket \
            = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.socket.bind((cf.SERVER_NAME, cf.SERVER_PORT))

        # This function returns handle
        return self.socket


    # interface
    def do_connect(self):

        try:
            # create socket
            handle = self._make_socket()

            self.socket.connect(cf.SERVER_NAME, cf.SERVER_PORT)

            # do work here.
            if self.do_connect_action == None:
                raise Exception

            self.do_connect_action(self.socket)

        except:
            print('\t[SocketPiClient] do_connect exception catched.')
            loggerd.log('do_connect exception.', 'client')

        finally:
            self._close_socket()
            
    # 
    # Registered function mush have a parameter.
    # socket!!
    def register_action(self, action):
        self.do_connect_action = action
    


# 
# Additional approach
# https://brownbears.tistory.com/207
# Socket handler
class SocketPiServer_TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        
        cur_thread = threading.current_thread()

        print("\t[Server] {} was started for {}".format( \
            cur_thread.getName(), self.client_address[0]))
        
        try: 
                #self.recv_data = self.request.recv(1024).strip()

                recv_buff = self.request.recv(1024).strip()
                    # Here, server receives data and put that into the buffer.
                    # recv_buff is a byte form.

                recv_data = str(recv_buff, encoding='utf-8')
                print('\t[Server] "{str}" received'.format(str=recv_data))
                loggerd.log('"{str}" received'.format(str=recv_data), 'server')

        except Exception as e:
            print('\t' + str(e))

        print("\t[Server] {} was ended for {}" .format(cur_thread.getName(), self.client_address[0]))

        pass





if __name__ == '__main__':
    
    loggerd.new()

    # First print banner
    print(cf.PROJECT_BANNER)
    print('\tExecuting config script. Running in debug mode.\n')

    # This is how you make server.
    server = SocketPiServer()
    server.doStart()
    
    server.doListenDaemon()
    # server.doStartListen()
    #server.do_listen()

    # time.sleep(1000)
    input()

    pass













