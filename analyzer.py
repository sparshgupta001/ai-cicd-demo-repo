from flask import Flask, request

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    logs = request.data.decode()

    print("\\n===== RECEIVED LOGS =====\\n")
    print(logs)

    return {
        "status": "received",
        "message": "Logs analyzed successfully"
    }

app.run(port=8000)