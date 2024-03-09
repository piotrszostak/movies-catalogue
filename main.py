from datetime import date

from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker

import tmdb_client
from models import Movie
from db import engine

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [get_movie_info(movie) for movie in tmdb_client.get_movies()]
    return render_template("homepage.html", movies=movies)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=details)

@app.route("/users/<user_id>")
def user_movies(user_id):
    response = {}
    user_movies = session.query(Movie).filter_by(user_id=user_id)   
    # TODO change to list comprehension 
    movie_list = []
    for movie in user_movies:
        dictionary = {
            "id": movie.id,
            "title": movie.title,
            "director": movie.director
        }
        movie_list.append(dictionary)
    
    response[user_id] = movie_list
    return response


@app.route("/movies", methods=["POST"])
def create_movie():
    # TODO marshmallow serializer(verify input data)
    input_dict = request.get_json()
    movie_instance = Movie(
        title=input_dict["title"],
        release_date=date.fromisoformat(input_dict["release_date"]), 
        director=input_dict["director"],
    )
    #movie_instance > db
    session.add(movie_instance)
    session.commit()
    session.close()
    return input_dict, 201

# add to favs
def add_movie_to_favs(movie_id, user_id):
    pass
# share favs with email

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(poster_path=path, size=size)
    return {"tmdb_image_url": tmdb_image_url}

def get_movie_info(movie):
    movie_info = {
        "id": movie["id"],
        "title": movie["title"],
        "poster": movie["poster_path"]
    }
    return movie_info

if __name__ == '__main__':
    app.run(debug=True)