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
# logging.py
# 

# necessary for directory address information, user.
import config as cf

# system
import os
import os.path
from datetime import date, datetime



# 
# Logger class
# Author: SukJoon Oh
class Logger_d:
    
    # 
    # Author's note:
    #
    # This class will be used as log-writing process.
    # This script is dependent on some configuration set in config.py file, 
    # thus make sure to include config.py
    #
    # This class counts log files as being constructed, 
    # checking latest file name to overwrite.
    # Be sure to have nothing or only log files in the LOG_DIR/logs directory,
    # or this will unintentionally might modify unwanted files.
    # 

    def countLogFiles(self):
        count = int(len(os.listdir(cf.LOG_DIR)))

        if count == 0: return 0
        else: return count - 1

    #
    # Loggger object sets file name to 'log-[date]-[file number]' format, 
    # which file number is set to the files exist in the target directory.
    # 
    # This class is simple as it is, thus it only counts any files exist in the 
    # target directory, thus if you don't want to mess the log file name number
    # order, be sure not to put something other than log files in the target directory.
    #
    def setFileName(self, offset):
        log_date = datetime.now()

        return cf.LOG_FILENAME_PREFIX \
            + '%s-%s-%s' % ( log_date.year, log_date.month, log_date.day ) + '-' \
            + str("%08d" % (self.countLogFiles() + offset))
    
    # public interface
    def new(self):
         
        if int(len(os.listdir(cf.LOG_DIR))) == 0:
            self.file_name = self.setFileName(0)
        else:
            self.file_name = self.setFileName(1)

        if cf.DEBUG_FLAG:
            #print('\tnew file: \t' + self.file_name)
            pass

    #
    # constructor
    def __init__(self):
        # Log file name will be set as 'log-[date]-0000000x'.
        # The class needs to be aware of the latest file number.
        self.file_name = self.setFileName(0)
        
        #
        # debug console
        if cf.DEBUG_FLAG:
            #print('\tfile name: \t' + self.file_name) 
            pass


    def log(self, message, cls = 'none'):

        # first make message format to, 
        #     [datetime][category][message]
        #     format. 

        # check if file exists
        log_file = cf.LOG_DIR + self.file_name

        with open(log_file, mode="a", encoding='utf-8') as file:
            file.write(str(datetime.now()).split('.')[0] + \
                '\t' + cls + '\t' \
                '\t' + message + '\n')

            
    # This seems unnecessary.
    def cancelLog(self):
        pass

    # added
    def history(self):

        # check if file exists
        log_file = cf.LOG_DIR + self.file_name

        with open(log_file, mode="r", encoding='utf-8') as file:
            
            while(True):
                 line = file.readline()
                 if not line: break
                 print('\t' + line, end='')


loggerd = Logger_d()


if __name__ == "__main__":
    
    pass

    #
    # This is a sample code for using Logger class.
    # 2019.10.30.

    # declare a Logger object. 
    # Singleton is highly suggested.
    sample_object = Logger_d()

    #sample_object.log('asfdasdfafds')
    sample_object.history()


     