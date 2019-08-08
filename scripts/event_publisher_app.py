#!/usr/bin/env python

import rospy
from EventPublisher import *


def publisher():

    rospy.init_node('publisher', anonymous=True)

    #default
    rate = 10
    #set up logger
    if rospy.has_param('~rate'):
        rate = rospy.get_param('~rate')

    pub = EventPublisher()
    
    # generate random msg in a loop with a given delay
    rospy.Timer(rospy.Duration(1. / rate), pub.publish_random_msg)

    rospy.spin()

if __name__ == '__main__':
    publisher()
