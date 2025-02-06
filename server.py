from flask import Flask, jsonify, request
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app) 

@app.route('/visitor_ip', methods=['GET'])
def visitor_ip():
    try:
        visitor_ip = request.remote_addr
        return jsonify({"visitor_ip": visitor_ip})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
