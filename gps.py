from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store the latest GPS data
gps_data = {"latitude": None, "longitude": None, "accuracy": None, "timestamp": None}

@app.route('/update_gps', methods=['POST'])
def update_gps():
    global gps_data
    data = request.json
    gps_data['latitude'] = data.get('lat')
    gps_data['longitude'] = data.get('lon')
    gps_data['accuracy'] = data.get('acc')
    gps_data['timestamp'] = data.get('tst')
    return jsonify(gps_data), 200

@app.route('/get_gps', methods=['GET'])
def get_gps():
    return jsonify(gps_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
