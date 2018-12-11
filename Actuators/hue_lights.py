import requests
import rospy
from std_msgs.msg import String
import json

class LightsNode:
	def __init__(self, topic_name, token, step, colors, light_id = 2):
		self.token = "eWTU4i2znjgq-rLuYnfk7MhiTC6EU85wb-8Ya2Td"
		self.light_id = str(light_id)
	        self.topic_name = topic_name
		self.step = step
		self.url = "https://192.168.0.160/api/" + self.token + "/lights"
		self.colors = colors
		rospy.init_node('rpi_1', anonymous=True)

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
		bnode.listen()

	rospy.spin()
#payload  = {'hue': 20000}
#response = requests.put("https://192.168.0.160/api/eWTU4i2znjgq-rLuYnfk7MhiTC6EU85wb-8Ya2Td/lights/2/state", data=json.dumps(payload), verify=False)
