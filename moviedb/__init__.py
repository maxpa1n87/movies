from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    movies = [{'Title':'Death Proof', 'Subtitle': 'Tot sicher', 'Author': 'Quentin Tarantino', 'Release': '2008', 'Description': 'Evil baddy movie',  }]
    return render_template('index.html', movies=movies)
