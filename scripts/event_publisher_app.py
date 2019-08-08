#!/usr/bin/env python

import rospy
from EventPublisher import *


def publisher():

    rospy.init_node('publisher', anonymous=True)

    #default
    rate = 10
    log_stdout = False

    #set up publisher params
    if rospy.has_param('~rate'):
        rate = rospy.get_param('~rate')
    if rospy.has_param('~log_stdout'):
        log_stdout = rospy.get_param('~log_stdout')

    pub = EventPublisher()
    pub.enable_std_output(log_stdout)


    
    # generate random msg in a loop with a given delay
    rospy.Timer(rospy.Duration(1. / rate), pub.publish_random_msg)

    rospy.spin()

if __name__ == '__main__':
    publisher()
