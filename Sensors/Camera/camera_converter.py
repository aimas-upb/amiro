#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class CameraConverter:

  def __init__(self, url = "rtsp://admin:admin@192.168.0.127/play1.sdp", publisher = "front_camera_topic"):
    self.image_pub = rospy.Publisher(publisher, Image)
    self.bridge = CvBridge()
    self.capture = cv2.VideoCapture(url)

  def publish():
    try:
      cv_image = self.capture.read()
    except CvBridgeError as e:
      print(e)
    cv2.waitKey(1)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = CameraConverter()
  rospy.init_node('camera_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)