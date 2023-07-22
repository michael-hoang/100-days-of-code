from wtforms import fields
from dotenv import load_dotenv
import os
import requests

load_dotenv()
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ.get('TMDB_API_READ_ACCESS_TOKEN')}",
}


# My helper functions
def get_poster_base_url_and_sizes() -> tuple[str, list]:
    """Request base image URL and list of image poster sizes."""
    url = "https://api.themoviedb.org/3/configuration"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return data["images"]["base_url"], data["images"]["poster_sizes"]


def is_filled(field: fields) -> bool:
    """
    Return True if field is not empty.

    raw_data:
    If form data is processed, is the valuelist given from the formdata wrapper.
    Otherwise, raw_data will be None.
    """
    try:
        value = field.raw_data[0]
    except TypeError:
        return False
    else:
        if value == "":
            return False
    return True


def search_movie(movie: str, page=1) -> dict:
    """Request TMDB API (https://api.themoviedb.org/3/search/movie) for movie data."""

    url = f"https://api.themoviedb.org/3/search/movie?query={movie}&page={page}"
    response = requests.get(url, headers=HEADERS)
    return response.json()
