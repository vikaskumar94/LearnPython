#Author: OMKAR PATHAK
#This script helps to build a simple stopwatch application using Python's time module.

import time

print('Press ENTER to begin, Press Ctrl + C to stop')

while True:
    try:
    	""" if you are running python 2.x use raw_input() instead of input()"""
        input()
        starttime = time.time()
        print('Started')
        
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        print('Total Time:', round(endtime - starttime, 2),'secs')
        break