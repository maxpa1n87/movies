from flask import Flask
from flask_login import LoginManager
from . import user

def create_app():
    app = Flask(__name__)

    with app.open_resource('secret_key') as f:
        app.secret_key = f.read().decode('utf8')

    login_manager = LoginManager()

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return user.User.get_id(user_id)
    
    from . import database
    database.init_db()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import moviedb
    app.register_blueprint(moviedb.bp)
    app.add_url_rule('/', endpoint='index')

    return app
