import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/api/live-meetings")
def get_live_meetings():
    access_token = request.cookies.get('access_token')
    if not access_token:
        return jsonify({"error": "User not authenticated"}), 401

    meeting_info = requests.get(
        "https://api.zoom.us/v2/users/me/meetings?type=live",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()
    return jsonify(meeting_info)

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
