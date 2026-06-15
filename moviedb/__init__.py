from flask import Flask
from moviedb.login import login_manager
from moviedb.shared.models import db
from moviedb import auth, movie, download
import os

def create_app():
    app = Flask(__name__)

    with app.open_resource('secret_key') as f:
        app.config['SECRET_KEY'] = f.read().decode('utf8')

    login_manager.init_app(app)

    with app.open_resource('database_uri') as f:
        app.config['SQLALCHEMY_DATABASE_URI'] = f.read().decode('utf8')

    with app.open_resource('upload_folder') as f:
        app.config['UPLOAD_FOLDER'] = f.read().decode('utf8')

    app.config['MAX_CONTENT_LENGTH'] =  8 * 1000 * 1000
    app.config['MAX_PAGES_PER_PAGE'] = 5

    db.init_app(app)

    with app.app_context():
        db.create_all()
   
    app.register_blueprint(auth.bp)

    app.register_blueprint(movie.bp)
    app.add_url_rule('/', endpoint='index')

    app.register_blueprint(download.bp)
    app.add_url_rule('/uploads/<name>', endpoint="download_file", build_only=True)
    
    return app
