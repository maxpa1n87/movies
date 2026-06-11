from flask_login import LoginManager
from moviedb.shared.models import db
from moviedb.users.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == int(user_id))).one_or_none()
    if user == None:
        return None
    print(user[0].id)
    print(type(user[0].id))
    return user[0]
