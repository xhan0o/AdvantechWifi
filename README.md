# Request Listener
Request listener

Hardware : Advantech Wise 4012 

Technology: Python-Flask

Motivation: Server integration or data processing

### Files
RequestListener.py : Works for every request , displays request data on commandline

AdvantechPostListener.py : Listens and maps 'Push Notifications(JSON)' to python list.


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

### JSON

__readings__ : dictonary 
``` json 
readings = [{"Data": "Sensor Data",
             "MAC": "Mac Address",
             "PE": "PE",
             "Time": "Time Stamp",
             "UID": "Device name",
             "id": 1}]
```

