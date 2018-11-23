#!/usr/bin/env python

from sense_hat import SenseHat
import time
import rospy
from std_msgs.msg import String

class ROSSenseHat:
	def __init__(self):
		self.sense = SenseHat()
		self.pub = rospy.Publisher('environment', String, queue_size=10)
	    	rospy.init_node('ros_sense_hat', anonymous=True)

	def get_data(self):
		rate = rospy.Rate(10) # 10hz
		while not rospy.is_shutdown():
			env_event = {}
			env_event['humidity'] = {'unit' : '%%rH', 'value' : self.sense.humidity}
			env_event['pressure'] = {'unit' : 'mmHg', 'value' : self.sense.pressure}
			env_event['temperature'] = {'unit' : 'C', 'value' : self.sense.temperature}
			env_event['timestamp'] = time.time()

			self.pub.publish(str(env_event))
			rate.sleep()

if __name__ == '__main__':
	try:
		rosNode = ROSSenseHat()
		rosNode.get_data()
	except rospy.ROSInterruptException:
		pass
 
