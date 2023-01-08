import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

WEB_FILE = './data/100_best_movies.html'


def read_web_file():
    """Open local web file and return BeautifulSoup object."""
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        print(f"You need to save the rendered HTML to {WEB_FILE}")
        exit()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


soup = read_web_file()
movie_tags = soup.find_all(name='h3', class_='jsx-4245974604')
top100 = []

for movie_tag in movie_tags:
    top100.append(movie_tag.text)
