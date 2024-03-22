from sqlalchemy.orm import sessionmaker

from db import engine
from models import Movie

Session = sessionmaker(bind=engine)
session = Session()

def serialize_movie(movie):
    movie_dict = {
        "id": movie.id,
        "title": movie.title,
        "director": movie.director,
        "release_date": str(movie.release_date)
    }
    return movie_dict

def show_user_movies(user_id):
    user_movies = session.query(Movie).filter_by(user_id=int(user_id))
    movie_list = [serialize_movie(movie) for movie in user_movies]
    return movie_list

