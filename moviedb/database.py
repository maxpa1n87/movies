from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from moviedb import app

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

with app.open_resource('database_uri') as f:
    app.config['SQLALCHEMY_DATABASE_URI'] = f.read().decode('utf8')

db.init_app(app)

with app.app_context():
    db.create_all()
