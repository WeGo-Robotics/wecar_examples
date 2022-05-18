#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

class camera_subscriber():
    def __init__(self):
        rospy.init_node("camera_subscriber", anonymous=True)
        self.bridge = CvBridge()
        self.lidar_sub = rospy.Subscriber("image_jpeg/compressed", CompressedImage, self.camera_CB)

        while not rospy.is_shutdown():
            rospy.spin()

    def camera_CB(self, data):
        frame = self.bridge.compressed_imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("frame", frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    CS = camera_subscriber()
