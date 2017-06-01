from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/io_log', methods=['POST'])
def hello():
        result = request.get_json(force=True)
   	print result
        return ('', 204)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True) #Defining IP and port. (Host IP on network)

