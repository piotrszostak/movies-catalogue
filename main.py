from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [get_movie_info(movie) for movie in tmdb_client.get_movies()]
    return render_template("homepage.html", movies=movies)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=details)

# add to favs
# list favs
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