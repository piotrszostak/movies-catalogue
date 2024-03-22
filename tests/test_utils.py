import datetime

from sqlalchemy.orm import sessionmaker

from movies_catalogue.models import Movie, User
from movies_catalogue.utils import serialize_movie, show_user_movies
from movies_catalogue.main import session

def test_serialize_movie():
    #given
    test_movie = Movie(
        id=1,
        title="test_title",
        release_date=datetime.date(2000, 1, 1), 
        director="test_director",
    )
    #when
    serialized = serialize_movie(test_movie)
    #then
    assert serialized == {
        "id": 1,
        "title": "test_title",
        "release_date": "2000-01-01",
        "director": "test_director"
    }


def test_show_user_movies():
    #given
    test_user = User(
        name="test_name"
    )
    session.add(test_user)
    session.commit()
    
    test_movie = Movie(
        title="test_title",
        release_date=datetime.date(2001, 2, 2), 
        director="test_director",
        user_id=test_user.id
    )
    session.add(test_movie)
    session.commit()
    movie_id = test_movie.id
    
    to_assert = show_user_movies(test_user.id)
    assert to_assert == [
        {
            "id": movie_id,
            "title": "test_title",
            "release_date": "2001-02-02",
            "director": "test_director"
        }
    ]
    session.close()
