from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"result": "No URL provided"})

    # 🚨 Fake checks
    if "@" in url:
        return jsonify({"result": "Fake URL (contains @)"})

    if "192.168" in url or "127.0.0.1" in url:
        return jsonify({"result": "Suspicious (IP address used)"})

    if url.count('.') > 3:
        return jsonify({"result": "Fake URL (too many subdomains)"})

    if "login" in url or "verify" in url or "bank" in url:
        return jsonify({"result": "Suspicious (phishing keyword)"})

    # ✅ Basic safe check
    if url.startswith("https://"):
        return jsonify({"result": "Likely Safe URL"})
    else:
        return jsonify({"result": "Not Secure (No HTTPS)"})

if __name__ == "__main__":
    app.run()






