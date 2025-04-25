import base64
import time

import jwt
from flask import Flask, request, redirect, jsonify
import requests
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv(".env")

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/api/live-meetings")
def get_live_meetings():
    """Fetch Zoom user details using access token."""
    access_token = request.cookies.get('access_token')
    if not access_token:
        return jsonify({"error": "User not authenticated"}), 401

    user_info = requests.get(
        "https://api.zoom.us/v2/users/me/meetings?type=live",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()
    return jsonify(user_info)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
