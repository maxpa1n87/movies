from flask_login import UserMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    def get_id(self):
        return str(self.id)
