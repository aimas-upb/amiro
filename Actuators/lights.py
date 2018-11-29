import requests
import rospy
from std_msgs.msg import String
import json

class LightsNode:
	def __init__(self, topic_name, token, step):
		self.token = "cde2e632edf55ac47e444523e12fb7807d6aaf51246f90f5cf6aa4be74efbad7"
	        self.topic_name = topic_name
		self.step = step
		self.headers = {
			"Authorization": "Bearer %s" % token,
		}
		rospy.init_node('rpi_1', anonymous=True)

	def listen(self):
		rospy.Subscriber(self.topic_name, String, self.on_lights_msg)

	def on_lights_msg(self, data):
		print(data.data)
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		payload = json.loads(data.data)
		if 'brightness' in payload:
			response = requests.get('https://api.lifx.com/v1/lights/all', headers=self.headers)
			payload['brightness'] = min(1.0, max(response.json()[0]['brightness'] + payload['brightness'] * self.step, 0.0))
		print(payload)
		response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=self.headers)


with open('lights_config.json') as json_data_file:
	lights_config = json.load(json_data_file)

	for key in lights_config:
		bnode = LightsNode(key, lights_config[key]['token'], lights_config[key]['step'])
		bnode.listen()

	rospy.spin()
