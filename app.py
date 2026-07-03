from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import sqlite3

from config import create_database

# Voice
from voice.voice_register import register_voice
from voice.voice_login import voice_login

# Face
from face.face_register import register_face
from face.face_login import login_face

# Dashboard
from admin.dashboard import get_dashboard_data

# Users
from admin.users import get_all_users, delete_user

# Reports
from reports.report import generate_pdf, generate_excel

app = Flask(__name__)
CORS(app)


# =====================================================
# Save Login History
# =====================================================

def save_login(username, method, status):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO login_history
        (username, method, status)
        VALUES (?, ?, ?)
        """,
        (username, method, status)
    )

    conn.commit()
    conn.close()


# =====================================================
# Home
# =====================================================

@app.route("/")
def home():

    return jsonify({
        "message": "SecurePass API Running Successfully"
    })


# =====================================================
# Voice Registration
# =====================================================

@app.route("/register", methods=["POST"])
def register_voice_route():

    data = request.get_json()

    username = data.get("username", "").strip()

    if username == "":
        return jsonify({
            "success": False,
            "message": "Username Required"
        })

    result = register_voice(username)

    if result:

        return jsonify({
            "success": True,
            "message": "Voice Registered Successfully"
        })

    return jsonify({
        "success": False,
        "message": "Voice Registration Failed"
    })


# =====================================================
# Voice Login
# =====================================================

@app.route("/login/voice", methods=["POST"])
def login_voice_route():

    data = request.get_json()

    username = data.get("username", "").strip()

    if username == "":
        return jsonify({
            "success": False,
            "message": "Username Required"
        })

    result = voice_login(username)

    if result:

        save_login(
            username,
            "Voice",
            "Success"
        )

        return jsonify({
            "success": True,
            "message": "Voice Login Successful"
        })

    save_login(
        username,
        "Voice",
        "Failed"
    )

    return jsonify({
        "success": False,
        "message": "Voice Login Failed"
    })


# =====================================================
# Face Registration
# =====================================================

@app.route("/register/face", methods=["POST"])
def register_face_route():

    data = request.get_json()

    username = data.get("username", "").strip()
    image = data.get("image", "")

    if username == "" or image == "":
        return jsonify({
            "success": False,
            "message": "Username and image are required."
        })

    result = register_face(username, image)

    if result:
        return jsonify({
            "success": True,
            "message": "Face Registered Successfully"
        })

    return jsonify({
        "success": False,
        "message": "Face Registration Failed"
    })

# =====================================================
# Face Login
# =====================================================

@app.route("/login/face", methods=["POST"])
def login_face_route():

    data = request.get_json()

    username = data.get("username", "").strip()
    image = data.get("image", "")

    if username == "" or image == "":
        return jsonify({
            "success": False,
            "message": "Username and image are required."
        })

    result = login_face(username, image)

    if result:

        save_login(
            username,
            "Face",
            "Success"
        )

        return jsonify({
            "success": True,
            "message": "Face Login Successful"
        })

    save_login(
        username,
        "Face",
        "Failed"
    )

    return jsonify({
        "success": False,
        "message": "Face Login Failed"
    })
# =====================================================
# Dashboard
# =====================================================

@app.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify(
        get_dashboard_data()
    )


# =====================================================
# Users
# =====================================================

@app.route("/users", methods=["GET"])
def users():

    return jsonify(
        get_all_users()
    )


@app.route("/delete-user/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):

    delete_user(user_id)

    return jsonify({
        "success": True
    })


# =====================================================
# PDF Report
# =====================================================

@app.route("/report/pdf")
def report_pdf():

    generate_pdf()

    return send_file(
        "reports/login_report.pdf",
        as_attachment=True
    )


# =====================================================
# Excel Report
# =====================================================

@app.route("/report/excel")
def report_excel():

    generate_excel()

    return send_file(
        "reports/login_report.xlsx",
        as_attachment=True
    )


# =====================================================
# Run Application
# =====================================================

if __name__ == "__main__":

    create_database()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )