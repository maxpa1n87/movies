from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from moviedb.database import db

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
