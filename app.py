from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Another change to be displayed on the home page"