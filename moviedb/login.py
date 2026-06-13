from flask_login import LoginManager
from moviedb.shared.models import db
from moviedb.users.models import User
from flask import redirect, url_for

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == int(user_id))).scalar()
    if user == None:
        return None
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))
