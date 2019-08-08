#!/usr/bin/env python

import rospy
from EventProcessor import *

def logger_client():

    rospy.init_node('listener', anonymous=True)

    #default params
    rate = 10
    file_name = '/home/logger_client_log.txt'
    log_stdout = False

    #set up params for logger
    if rospy.has_param('~rate'):
        rate = rospy.get_param('~rate')
    if rospy.has_param('~file_name'):
        file_name  = rospy.get_param('~file_name')
    if rospy.has_param('~log_stdout'):
        log_stdout = rospy.get_param('~log_stdout')

    logg = EventProcessor(int(rate), file_name)
    
    logg.enable_std_output(log_stdout)

    #run loop
    logg.start()

if __name__ == '__main__':
    logger_client()
