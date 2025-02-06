from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_arp', methods=['GET'])
def run_arp():
    try:
        result = subprocess.run(['netstat', '-ant'], capture_output=True, text=True)
        return jsonify({"output": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
