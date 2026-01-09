from flask import Flask, jsonify
from flask_cors import CORS
from voice.voice_login import voice_login

app = Flask(__name__)
CORS(app)   # 👈 IMPORTANT

@app.route("/login/voice", methods=["POST"])
def voice_auth():
    result = voice_login()
    return jsonify({"success": result})

if __name__ == "__main__":
    app.run(debug=True)
