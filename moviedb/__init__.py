from flask import Flask
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    from moviedb import database
    with app.app_context():
        database.init_db() 

    with app.open_resource('secret_key') as f:
        app.secret_key = f.read().decode('utf8')

    login_manager = LoginManager()

    login_manager.init_app(app)
    
    from moviedb import movie
    app.register_blueprint(movie.bp)
    app.add_url_rule('/', endpoint='index')

    from moviedb import auth
    app.register_blueprint(auth.bp)

    from moviedb.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.get_id(user_id) 
    
    return app
