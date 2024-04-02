from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"result": [0.2, 0.99, 0.5, 0.4]}
