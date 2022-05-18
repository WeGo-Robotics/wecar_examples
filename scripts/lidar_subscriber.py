#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import math

class lidar_subscriber():
    def __init__(self):
        rospy.init_node("lidar_subscriber", anonymous=True)
        self.lidar_sub = rospy.Subscriber("scan", LaserScan, self.lidar_CB)

        while not rospy.is_shutdown():
            rospy.spin()

    def lidar_CB(self, data):
        for (i, value) in enumerate(data.ranges):
            angle = (data.angle_min + i * data.angle_increment) * 180 / math.pi ## rad 2 deg
            if  -0.5 < angle < 0.5:
                print("(x, y) = ({}, {})".format(value * math.cos(angle*math.pi/180), value*math.sin(angle*math.pi/180)))
                print("(r, theta) = ({} ,  {})".format(value, angle)) 

if __name__ == '__main__':
    LS = lidar_subscriber()
