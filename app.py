from flask import Flask, render_template, jsonify

app = Flask(__name__)
@app.route("/")
def HomePage():
    return render_template("home.html")


if(__name__ == "__main__"):
    app.run("0.0.0.0",5000,debug= True)