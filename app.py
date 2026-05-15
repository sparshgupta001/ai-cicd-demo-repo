from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running"

# FORCE FAILURE
raise Exception("Intentional CI/CD Failure")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)