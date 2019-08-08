#!/usr/bin/env python

import rospy
from EventProcessor import *

def logger_client():

    rospy.init_node('listener', anonymous=True)
    #defaults
    rate = 10
    file_name = '/home/logger_client_log.txt'
    #set up logger
    if rospy.has_param('~rate'):
        rate = rospy.get_param('~rate')
    if rospy.has_param('~filename'):
        file_name  = rospy.get_param('~file_name')

    logg = EventProcessor(int(rate), file_name)
    
    #run loop
    logg.start()

if __name__ == '__main__':
    logger_client()
