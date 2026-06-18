from flask import Flask
from moviedb.login import login_manager
from moviedb.shared.models import db
from moviedb import auth, movie, download
from sqlalchemy.exc import OperationalError

def create_app():
    app = Flask(__name__)

    if app.config['DEBUG']:
        app.config.from_object('moviedb.default_settings')
    else:
        app.config.from_envvar('MOVIEDB_SETTINGS')

    login_manager.init_app(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()
                   
    app.register_blueprint(auth.bp)

    app.register_blueprint(movie.bp)
    app.add_url_rule('/', endpoint='index')

    app.register_blueprint(download.bp)
    app.add_url_rule('/uploads/<name>', endpoint="download_file", build_only=True)
    
    return app
