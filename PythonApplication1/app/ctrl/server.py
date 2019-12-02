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


from socket_pi import SocketPi

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



    # Parameter: None
    # Returns: Handle
    # Author: acoustikue(SukJoon Oh)
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



    # Parameter: None
    # Returns: -
    # Author: acoustikue(SukJoon Oh)
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
    # Parameter: None
    # Returns: 
    # Author: acoustikue(SukJoon Oh)
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



    # Parameter: None
    # Returns: -
    # Author: acoustikue(SukJoon Oh)
    def doListenDaemon(self):

        # This function starts watchdog member function.
        # Watchdog starts serve_forever() as a daemon, so that,
        # the program flows independent from waiting client.
        notify_thread = threading.Thread(target=self._daemonWatchdog)
        notify_thread.daemon = True 
        notify_thread.start()

        # self._daemonWatchdog()

    def _daemonWatchdog(self):

        server_thread = threading.Thread(target=server.doListen)
        server_thread.daemon = True 
        server_thread.start()

        cnt = 0

        while(1):
            print('\t[Daemon] Daemon watchdog running. {name} alive: {stat}'.format( \
                name=server_thread.getName(), stat=server_thread.isAlive()))
            time.sleep(10)

         

    #
    # Multi client management
    def _m_client_handler(self, client_sock, addr):
        pass




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













