import datetime
from typing import List, Optional
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship
from db import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    movies: Mapped[List["Movie"]] = relationship(back_populates="user")
    
    def __repr__(self) -> str:
        return f"User: {self.name}, id: {self.id}"


class Movie(Base):
    __tablename__ = "movie"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(50))
    release_date: Mapped[datetime.date] = mapped_column(Date)
    director: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))
    user: Mapped[Optional["User"]] = relationship(back_populates="movies")
    
    def __repr__(self) -> str:
        return f"Movie: {self.title}, {self.release_date}"

Base.metadata.create_all(engine)
