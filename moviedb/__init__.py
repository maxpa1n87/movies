from flask import Flask
from moviedb.login import login_manager
from moviedb.shared.models import db
from moviedb import auth, movie
import os
import moviedb

def create_app():
    app = Flask(__name__)
    with app.open_resource('secret_key') as f:
        app.secret_key = f.read().decode('utf8')

    login_manager.init_app(app)

    with app.open_resource('database_uri') as f:
        app.config['SQLALCHEMY_DATABASE_URI'] = f.read().decode('utf8')

    app.config['UPLOAD_FOLDER'] = os.path.join('moviedb', os.path.join('static', 'uploads'))

    db.init_app(app)

    with app.app_context():
        db.create_all()
   
    app.register_blueprint(auth.bp)

    app.register_blueprint(movie.bp)
    app.add_url_rule('/', endpoint='index')

    return app
