from flask import Flask, jsonify
from flask import abort,make_response,request
import datetime


app = Flask(__name__)
def whatnow():
	now = datetime.datetime.now()
	datestr=now.strftime("%m-%d-%Y")
	timestr=now.strftime("%H:%M:%S")
	return datestr,timestr

#Defining dict
readings = [
    {
        'id': 1,
	'value1':u'number1',
	'value2':u'number2',
	'date':u'05-25-2017',
        'time': u'timestamp'
    },
    {
        'id': 2,
        'value1':u'number1',
        'value2':u'number2',
	'date':u'05-26-2017',
	'time': u'timestamp'
    }
]


#GET req
@app.route('/test/api/v1.0/sensor1', methods=['GET'])
def get_projects():
    return jsonify({'readings': readings})

#GET req for specific ID
@app.route('/test/api/v1.0/sensor1/<int:reading_id>', methods=['GET'])
def get_reading(reading_id):
    reading = [reading for reading in readings if reading['id'] == reading_id]
    if len(reading) == 0:
        abort(404)
    return jsonify({'reading': reading[0]})

#Error handler for abort(404) 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


#POST req. add value1,vlaue2 , date-time will be taken current fron system. id will be +1
@app.route('/test/api/v1.0/sensor1', methods=['POST'])
def create_project():
    if not request.json or not 'value1' in request.json:
        abort(400)
    datestr,timestr=whatnow()
    reading = {
        'id': readings[-1]['id'] + 1,
        'value1': request.json['value1'],
        'value2': request.json.get('value2', ""),
	'date': datestr,
	'time': timestr
    }
    readings.append(reading)
    return jsonify({'reading': reading}), 201

#PUT req. Update any paraments by id number.
@app.route('/test/api/v1.0/sensor1/<int:reading_id>', methods=['PUT'])
def update_reading(reading_id):
    reading = [reading for reading in readings if reading['id'] == reading_id]
    if len(reading) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'vlaue1' in request.json and type(request.json['value1']) != unicode:
        abort(400)
    if 'value2' in request.json and type(request.json['value2']) is not unicode:
        abort(400)
    if 'date' in request.json and type(request.json['date']) is not unicode:
        abort(400)
    if 'time' in request.json and type(request.json['time']) is not unicode:
	abort(400)
    project[0]['value1'] = request.json.get('value1', reading[0]['value1'])
    project[0]['value2'] = request.json.get('value2', reading[0]['value2'])
    project[0]['date'] = request.json.get('date', project[0]['date'])
    project[0]['time'] = request.json.get('time', project[0]['time'])
    return jsonify({'reading': reading[0]})

#DELETE req. Delete by id number.
@app.route('/test/api/v1.0/sensor1/<int:reading_id>', methods=['DELETE'])
def delete_reading(reading_id):
    reading = [reading for reading in projects if reading['id'] == reading_id]
    if len(reading) == 0:
        abort(404)
    readings.remove(reading[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
