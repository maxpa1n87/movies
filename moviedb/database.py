from flask import current_app, g 
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
    pass

def init_db():
    
    db = SQLAlchemy(model_class=Base)

    with current_app.open_resource('database_uri') as f:
        current_app.config['SQLALCHEMY_DATABASE_URI'] = f.read().decode('utf8')
    
    db.init_app(current_app)
    
    with current_app.app_context():
        db.create_all()
        g.db = db

    return g.db

def get_db():
    if 'db' not in g:
        init_db()
    return g.db
