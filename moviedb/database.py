from flask import g, current_app
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def init_db():
    # global db
    with current_app.open_resource('database_uri') as f:
        current_app.config['SQLALCHEMY_DATABASE_URI'] = f.read().decode('utf8')
    db.init_app(current_app)
    with current_app.app_context():
        db.create_all()
        g.db = db

    return g.db

def get_db():
    with current_app.app_context():
        if 'db' not in g:
            init_db()

    return g.db
