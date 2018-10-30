CAMI Gateway Configuration
==========================

### Gateway access
  - You must be connected on the local Wifi - precis308_24 or precis308_5
  - The IP address of the Gateway is locked to: 192.168.0.132
  - The username for SSH access is: `cami`
  
### Endpoint configuration
In the home directory of the `cami` user there is a file called: things.json.
Open the file and find the `endpoint` entry.
Add your new endpoint in the config.

The Gateway will send information in the following way:
  - on the path: `http://<your_endpoint>/measurements/` - data about health measurements collected from the Bluetooth sensors
    connected to the CAMI Gateway (weight scale, BP monitor)
  - on the path: `http://<your_endpoint>/events/` - data about events detected by the Z-Wave sensors 
    connected to the Gateway (Fibaro motion sensor, door/window sensor - these can also send 
    temperature and luminosity information)

The messages format is defined in the following 
[API definition file](https://github.com/cami-project/cami-project/blob/master/insertion/cami-insertion-api.yml).
To view the file in pretty printing, open https://editor.swagger.io/ and copy paste 
the contents of the yml file in the left pane.

  
  
