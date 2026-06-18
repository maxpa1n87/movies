from flask import Flask
from moviedb.login import login_manager
from moviedb.shared.models import db
from moviedb import auth, movie, download
from moviedb import error_handlers

def create_app():
    app = Flask(__name__)

    if app.config['DEBUG']:
        app.config.from_object('moviedb.default_settings')
    else:
        app.config.from_envvar('MOVIEDB_SETTINGS')

    app.register_error_handler(404, error_handlers.page_not_found)
    app.register_error_handler(405, error_handlers.method_not_allowed)
    app.register_error_handler(413, error_handlers.request_entity_too_large)

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

if __name__ == '__main__':
    create_app()
