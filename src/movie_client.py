import requests
import os


def get_movie(movie_id):
    r = requests.get('http://www.omdbapi.com',
                     {'apikey': os.environ.get('MOVIE_API_KEY'),
                      'i': movie_id})
    if r.status_code == 200:
        return r.json()
    else:
        return None


def list_movies():
    # TODO
    pass
