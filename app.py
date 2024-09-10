from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Global dictionaries to store payloads for device 1,2,3 and 4
device_data = {
    1: None,
    2: None,
    3: None,
    4: None
}

@app.route('/api/receive_data', methods=['POST'])
def receive_data():
    """
    Route to process received data and store it based on device_number.
    """
    data = request.get_json()

    if data:
        device_number = data.get('device_number')
        if device_number in [1, 2]:
            device_data[device_number] = data  # Save data for the specific device
            print(f"Received data for Device {device_number}: {data}")

            try:
                # Load existing data if the file exists
                if os.path.exists('data/phrase.json'):
                    with open('data/phrase.json', 'r', encoding='utf-8') as file:
                        try:
                            saved_data = json.load(file)
                            # Ensure that the loaded data is a list
                            if not isinstance(saved_data, list):
                                saved_data = [saved_data]
                        except json.JSONDecodeError:
                            saved_data = []
                else:
                    saved_data = []

                # Append the new data to the list
                saved_data.append(data)

                # Save updated data to the file
                with open('data/phrase.json', 'w', encoding='utf-8') as file:
                    json.dump(saved_data, file, indent=4)

                return jsonify({"message": "Data received and saved successfully"}), 200
            except Exception as e:
                print(f"Error saving data to file: {e}")
                return jsonify({"error": "Failed to save data to file"}), 500
        else:
            return jsonify({"error": "Invalid device_number"}), 400

    return jsonify({"error": "No JSON data received"}), 400

@app.route('/api/device_data/<int:device_number>')
def get_device_data(device_number):
    """
    Route to return the last payload for the specific device.
    """
    if device_number in [1, 2] and device_data[device_number]:
        return jsonify(device_data[device_number])
    return jsonify({"error": f"No data for device {device_number}"}), 404

@app.route('/')
def index():
    """
    Render the index page showing data for both devices.
    """
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')

    app.run(host='0.0.0.0', debug=True, port=5001)