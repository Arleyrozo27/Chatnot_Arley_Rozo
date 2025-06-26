from flask import Flask, request, jsonify, send_from_directory
from chatbot import responder

app = Flask(__name__, static_folder='frontend')

@app.route("/")
def index():
    return send_from_directory('frontend', 'index.html')

@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory('frontend', path)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = responder(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)