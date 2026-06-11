from flask_login import LoginManager
from moviedb.shared.models import db
from moviedb.users.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == int(user_id))).scalar()
    if user == None:
        return None
    return user
