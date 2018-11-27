#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class CameraConverter:

  def __init__(self, url = "rtsp://admin:admin@192.168.0.127/play1.sdp", publisher = "entry_camera"):
    self.image_pub = rospy.Publisher(publisher, Image, queue_size=10)
    self.bridge = CvBridge()
    self.capture = cv2.VideoCapture(url)

  def publish(self):
    try:
      cv_image = self.capture.read()
    except CvBridgeError as e:
      print(e)
    print(type(cv_image))

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image[1], "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = CameraConverter()
  rospy.init_node('camera_converter', anonymous=True)
  try:
    while not rospy.is_shutdown():
        ic.publish()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
