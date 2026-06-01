from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    movies = [{'Title':'Death Proof', 'Description': 'Evil baddy movie', 'Release': "2008" }]
    return render_template('index.html', movies=movies)
