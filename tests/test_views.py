import datetime
from movies_catalogue.main import app, session
from movies_catalogue.models import Movie, User

client = app.test_client()

def test_create_movie():
    #given
    request_data = {
        "title": "test_title",
        "release_date": "2001-03-03",
        "director": "test_director"
    }
    test_response = client.post("/movies", json=request_data)
    
    assert session.get(Movie, test_response.json["id"])
    assert test_response.json["title"] == "test_title"
    assert test_response.json["release_date"] == "2001-03-03"
    assert test_response.json["director"] == "test_director"
    
    
def test_add_to_favs():
    #create instance Movie and User
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
    
    #client.post (json = movie_id, user_id)
    test_movie_id = test_movie.id
    test_user_id = test_user.id
    test_respone = client.post("/favs", json={"movie_id": test_movie_id, "user_id": test_user_id})
    #assert Movie has user_id == test_user.id
    test_movie = session.get(Movie, test_movie_id)
    test_user = session.get(Movie, test_user_id)
    assert test_movie.user_id == test_user.id
    #assert response has one dict in a list [{}]
    assert test_respone.json == [
        {
            "id": test_movie_id,
            "title": "test_title",
            "release_date": "2001-02-02",
            "director": "test_director"
        }
    ]
    session.close()