from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

@app.route("/")
def dashboard():
    data = [31, 40, 28, 51, 42, 82, 56]
    return render_template('index.html', data=data)