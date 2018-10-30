import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO           # import RPi.GPIO module
import json


class BlindsNode:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD

		with open('blinds_config.json') as json_data_file:
			gpio_config = json.load(json_data_file)

		self.gpio_up = gpio_config['blinds']['up']
		self.gpio_down = gpio_config['blinds']['down']

		for gpio in self.gpio_down + self.gpio_up:
			GPIO.setup(gpio, GPIO.OUT, pull_up_down=GPIO.PUD_UP)

	def listener(self):
		rospy.init_node('rpi1', anonymous=True)

		rospy.Subscriber("blinds", String, self.on_blinds_msg)

		# spin() simply keeps python from exiting until this node is stopped
		rospy.spin()

	def on_blinds_msg(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		command = json.loads(data.data)

		if not 'blinds' in command:
			rospy.loginfo("Wrong command")
			return

		if command['blinds'] == -1:
			for gpio in self.gpio_down:
				GPIO.output(gpio, 1)
		elif command['blinds'] == 1:
			for gpio in self.gpio_up:
				GPIO.output(gpio, 1)
		else:
			for gpio in self.gpio_up + self.gpio_down:
				GPIO.output(gpio, 0)

bnode = BlindsNode()
bnode.listener()