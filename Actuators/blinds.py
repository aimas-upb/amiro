import rospy
from std_msgs.msg import Int32
from amiro_services.srv import IsAvailable, IsAvailableResponse

import RPi.GPIO as GPIO
import json


class BlindsNode:
	ROS_NODE_NAME = "rpi_1"

	def __init__(self, topic_name, gpio_up, gpio_down):
		GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
		rospy.init_node('rpi_1', anonymous=True)
		self.topic_name = topic_name
		self.gpio_up = gpio_up
		self.gpio_down = gpio_down

		GPIO.setup(gpio_up, GPIO.OUT, initial=1)
		GPIO.setup(gpio_down, GPIO.OUT, initial=1)

		# setup availability service
		self.availability_service = None
		self.__setup_availability_service()


	def __setup_availability_service(self):
		service_name = BlindsNode.ROS_NODE_NAME + "_availability"
		self.availability_service = rospy.Service(service_name, IsAvailable, self.is_available)


	def is_available(self):
		return IsAvailableResponse(True)


	def listen(self):
		rospy.Subscriber(self.topic_name, Int32, self.on_blinds_msg)

	def on_blinds_msg(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		GPIO.output(self.gpio_up, 1);
		GPIO.output(self.gpio_down, 1);

		if data.data == -1:
			GPIO.output(self.gpio_down, 0)
		elif data.data == 1:
			GPIO.output(self.gpio_up, 0)

with open('blinds_config.json') as json_data_file:
	gpio_config = json.load(json_data_file)

for key in gpio_config:
	bnode = BlindsNode(key, gpio_config[key]['up'], gpio_config[key]['down'])
	bnode.listen()

rospy.spin()
