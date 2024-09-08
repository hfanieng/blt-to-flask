from flask import Flask, request

app = Flask(__name__)

@app.route('/api/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(data)
    return "Data received successfully"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
