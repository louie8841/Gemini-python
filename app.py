from flask import Flask, render_template, request, jsonify
import urllib.request
import json

app = Flask(__name__)

API_KEY = "AIzaSyD5k7dO2fEzxlCC5y5lkxyap39-tXqfLSE"  # 본인 키로 바꾸세요
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

history = []

def call_gemini_api(history):
    contents = [{"role": h["role"], "parts": [{"text": h["text"]}]} for h in history]
    data = {"contents": contents}
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(API_URL, data=json_data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            reply = result["candidates"][0]["content"]["parts"][0]["text"]
            return reply
    except urllib.error.HTTPError as e:
        return f"[HTTP Error {e.code}] {e.read().decode()}"
    except Exception as e:
        return f"[Error] {e}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global history
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    history.append({"role": "user", "text": user_input})
    reply = call_gemini_api(history)
    history.append({"role": "model", "text": reply})

    return jsonify({"response": reply})

@app.route("/reset", methods=["POST"])
def reset():
    global history
    history = []
    return jsonify({"status": "reset success"})

if __name__ == "__main__":
    app.run(debug=True)
