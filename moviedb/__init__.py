from flask import Flask
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
with app.open_resource('secret_key') as f:
    app.secret_key = f.read().decode('utf8')

login_manager = LoginManager()

login_manager.init_app(app)

db = SQLAlchemy(model_class=Base)

with app.open_resource('database_uri') as f:
    app.config['SQLALCHEMY_DATABASE_URI'] = f.read().decode('utf8')

db.init_app(app)

with app.app_context():
    db.create_all()

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    
@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)

from moviedb import auth
app.register_blueprint(auth.bp)

from moviedb import movie
app.register_blueprint(movie.bp)
app.add_url_rule('/', endpoint='index')
