import requests

def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjE5ZDVhMWI4ODQ1NjMyNTZhNWIzYTY1MGMxZDI3YyIsInN1YiI6IjY1YmE1NmIxZTlkYTY5MDEyZGYyY2YyZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7ScUMOxnQjwjLIv1EYgK0IEUzXHhEx4Owm5llTduM00"
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjE5ZDVhMWI4ODQ1NjMyNTZhNWIzYTY1MGMxZDI3YyIsInN1YiI6IjY1YmE1NmIxZTlkYTY5MDEyZGYyY2YyZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7ScUMOxnQjwjLIv1EYgK0IEUzXHhEx4Owm5llTduM00"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_path, size="w342"):
    return f"https://image.tmdb.org/t/p/{size}{poster_path}"