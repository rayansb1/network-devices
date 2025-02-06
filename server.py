from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/get_ip', methods=['GET'])
def get_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return jsonify({"hostname": hostname, "ip_address": ip_address})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
