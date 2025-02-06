from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_arp')
def run_arp():
    try:
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        return jsonify({"output": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
