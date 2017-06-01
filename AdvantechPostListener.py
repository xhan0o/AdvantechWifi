
from flask import Flask, request, jsonify
from pprint import pprint
import csv
app = Flask(__name__)

readings=[{'id': 1,
                'Time': "TIme Stamp",
                'Data': "Sensor Data",
                'MAC': "Mac Address",
                'UID':  "Device name",
                'Pe':  "PE"
		}
	]

#uniquetime=[]

def writecsv():
	with open('sensor1.csv', 'wb') as myfile:
    		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    		wr.writerow(readings)
	return

@app.route('/io_log', methods=['POST'])
def hello():
	result = request.get_json(force=True)
	#Utime=request.get_json().get(u'TIM',"")	
	#for timestamp in uniquetime:
	#	if Utime != timestamp:
	#		print "xxx"
	#		uniquetime.append(Utime)
	#	elif Utime == timestamp:
	#		print "Duplicate entry"
	#	else:
	#		print "z"
	#print uniquetime		
	reading = {
		'id':readings[-1]['id'] + 1,
		'Time': request.get_json().get(u'TIM',""),
		'Data': request.get_json().get(u'Record',""),
		'MAC': request.get_json().get(u'MAC',""),
		'UID':  request.get_json().get(u'UID',""),
		'Pe':  request.get_json().get(u'PE',"")
		}
		
	print "RAW Request" + str(request.get_json())
    	readings.append(reading)
	pprint (readings)
	#writecsv()	
	return ('', 204)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True) #Defining IP and port. (Host IP on network)

