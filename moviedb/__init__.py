from flask import Flask
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import moviedb
    app.register_blueprint(moviedb.bp)
    app.add_url_rule('/', endpoint='index')

    with open(__name__ + '/secret_key') as f:
        app.secret_key = f.read()

    login_manager = LoginManager()

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    
    return app
