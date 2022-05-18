#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

class drive_publisher():
    def __init__(self):
        rospy.init_node("drive_publisher", anonymous=True)
        self.drive_pub = rospy.Publisher("vesc/high_level/ackermann_cmd_mux/input/nav_0", AckermannDriveStamped, queue_size=5)
        self.rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            drive_msg = AckermannDriveStamped()
            drive_msg.header.stamp = rospy.Time.now()
            drive_msg.drive.speed = 1.0
            drive_msg.drive.steering_angle = 0.1
            self.drive_pub.publish(drive_msg)

if __name__ == '__main__':
    DP = drive_publisher()
