from flask import Flask

app = Flask(__name__)

@app.route("/members")
def memebers():
    return "hand"

if __name__=="main":
    app.run(debug=True)