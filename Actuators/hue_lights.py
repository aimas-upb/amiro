import requests
import rospy
from std_msgs.msg import String
import json
from amiro_services.srv import IsAvailable, IsAvailableResponse
from amiro_services.msg import Availability


class LightsNode:
	ROS_NODE_NAME = "rpi_1"

	def __init__(self, topic_name, token, step, colors, light_id = 2):
		self.token = "eWTU4i2znjgq-rLuYnfk7MhiTC6EU85wb-8Ya2Td"
		self.light_id = str(light_id)
		self.topic_name = topic_name
		self.step = step
		self.url = "https://192.168.0.160/api/" + self.token + "/lights"
		self.colors = colors
		rospy.init_node('rpi_1', anonymous=True)

		service_root_name = LightsNode.ROS_NODE_NAME + "/" + self.topic_name
		self.__setup_availability_services(service_root_name)

	def __setup_availability_services(self, service_root_name):
		availability_service_name = service_root_name + "/is_available"
		availability_topic_name = service_root_name + "/availability"

		# setup the service
		self.availability_service = \
			rospy.Service(availability_service_name, IsAvailable, self.is_available)

		# setup the publisher
		self.availability_publisher = \
			rospy.Publisher(availability_topic_name, Availability, queue_size=10)

	def is_available(self, request):
		return IsAvailableResponse(True)

	def announce_available(self):
		msg = Availability()
		msg.is_available = True

		if self.availability_publisher:
			self.availability_publisher.publish(msg)


	def listen(self):
		rospy.Subscriber(self.topic_name, String, self.on_lights_msg)

	def on_lights_msg(self, data):
		print(data.data)
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		payload = json.loads(data.data)
		if 'brightness' in payload:
			response = requests.get(self.url, verify=False)
			print(response.json())
			payload['bri'] = min(254, max(response.json()[self.light_id]['state']['bri'] + payload['brightness'] * self.step, 0))
			del payload['brightness']

		if('power' in payload):
			if payload['power'] == 'off':
				payload['on'] = False
			else:
				payload['on'] = True
			del payload['power']

		if('color' in payload):
			if payload['color'] in self.colors:
				payload = self.colors[payload['color']]
		print(payload)

		response = requests.put(self.url + '/' + self.light_id + '/state', data=json.dumps(payload), verify=False)
		print(self.url + '/' + self.light_id + '/state')
		print(response)


with open('lights_config.json') as json_data_file:
	lights_config = json.load(json_data_file)

	for key in lights_config:
		bnode = LightsNode(key, lights_config[key]['token'], lights_config[key]['step'], lights_config[key]['colors'])
		bnode.announce_available()
		bnode.listen()

	rospy.spin()
#payload  = {'hue': 20000}
#response = requests.put("https://192.168.0.160/api/eWTU4i2znjgq-rLuYnfk7MhiTC6EU85wb-8Ya2Td/lights/2/state", data=json.dumps(payload), verify=False)
