from moviedb.shared.models import db
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
