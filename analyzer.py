from flask import Flask, request

app = Flask(__name__)

@app.route("/api/webhook", methods=["POST"])
def webhook():

    data = request.json

    print("\n===== GITHUB WEBHOOK RECEIVED =====\n")

    print("Source:", data.get("source"))
    print("Repository:", data.get("repo"))
    print("Run ID:", data.get("run_id"))
    print("Branch:", data.get("ref"))

    return {
        "status": "received",
        "message": "Webhook processed successfully"
    }

app.run(host="0.0.0.0", port=8000)