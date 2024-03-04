import datetime
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from db import engine

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# TODO user model 
# TODO relation to movie M2M

class Movie(Base):
    __tablename__ = "movie"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(50))
    release_date: Mapped[datetime.date] = mapped_column(Date)
    director: Mapped[str] = mapped_column(String(20))
    
    def __repr__(self) -> str:
        return f"Movie: {self.title}, {self.release_date}"
    
Base.metadata.create_all(engine)

movie1 = Movie(title="MovieTitle", release_date = datetime.date(2024, 2, 22), director="K.Waszkiewicz")
movie2 = Movie(title="Piraci z Karaibów", release_date = datetime.date(2010, 2, 3), director="M.Świtajło")
session.add(movie1)
session.add(movie2)
session.commit()
movies = session.query(Movie).filter_by(director="M.Świtajło")
print(movies.all())
session.close()
