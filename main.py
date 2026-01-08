from flask import Flask, jsonify
from flask_cors import CORS  # Ye zaroori hai
import requests

app = Flask(__name__)
CORS(app)  # Isse Loading khatam ho jayegi

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Daman API link
        url = "https://damanvipofficialhelp-spec.github.io/Daman-V5-Auto-AI/data.json" 
        response = requests.get(url, timeout=5)
        data = response.json()
        return jsonify({"status": "Succeed", "data": data})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

