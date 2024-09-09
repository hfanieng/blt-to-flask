from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/api/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    global last_payload
    if data:
        last_payload = data
        print("Received data:", data)
        return jsonify({"message": "Data received successfully"}), 200
    return jsonify({"error": "No JSON data received"}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_payload')
def get_payload():
    return jsonify(last_payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)