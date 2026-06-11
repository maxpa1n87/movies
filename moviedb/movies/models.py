from moviedb.shared.models import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    subtitle: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    release: Mapped[datetime] = mapped_column()
