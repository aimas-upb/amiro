import requests

token = "cde2e632edf55ac47e444523e12fb7807d6aaf51246f90f5cf6aa4be74efbad7"

headers = {
    "Authorization": "Bearer %s" % token,
}


for i in range(20,255):
    payload = {
        "brightness": i,
        "power" :"on"
    }
    print(payload)
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)