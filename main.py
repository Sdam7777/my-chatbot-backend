from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data
users = {
    "malik": "1234",
    "admin": "admin123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if users.get(data['username']) == data['password']:
        return jsonify({"success": True})
    return jsonify({"success": False}), 401

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json.get("message")
    return jsonify({"reply": f"Kamu bilang: {prompt}"})

@app.route("/")
def home():
    return "Backend aktif di Railway!"
