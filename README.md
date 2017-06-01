# Request Listener
Request listener
Hardware : Advantech Wise 4012 
Technology: Python-Flask
Motivation: Server integration or data processing

### Set up python-flask on Raspberry pi 
1. Installing pip
```bash
pi@raspberrypi ~ $ sudo apt-get install python-pip
```
2. Installing Flask 
```bash
pi@raspberrypi ~ $ sudo pip install flask
```

### Run Server
```bash 
pi@raspberrypi ~ $ sudo python RequestListner.py
 * Running on http://0.0.0.0:80/ 
 * Restarting with reloader
 
```
Server will start at ip of host (you can find that by __ifconfig__)

### APIs

__readings__ : dictonary 
``` json 
[{'Data': 'Sensor Data',
  'MAC': 'Mac Address',
  'Pe': 'PE',
  'Time': 'TIme Stamp',
  'UID': 'Device name',
  'id': 1}
]
```

