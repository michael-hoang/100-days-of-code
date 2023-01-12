# Create a Spotify Playlist using the Musical Time Machine

## Step 1 - Scraping the Billboard Hot 100

1. Create a new project in PyCharm and create the main.py file.

2. Create an `input()` prompt that asks what year you would like to travel to in YYY-MM-DD format. e.g.

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_14-52-50-8e0ee81dcf0c074e6234192486d69407.png" width="1000" />

3. Using what you've learnt about BeautifulSoup, scrape the top 100 **song titles** on that date into a Python List.

Hint: Take a look at the URL of the chart on a historical date: https://www.billboard.com/charts/hot-100/2000-08-12


## Step 2 - Authentication with Spotify
1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:

https://developer.spotify.com/dashboard/

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-15-28-7129f795b8f9ed2252e4deaa7b1fa913.png" width="400" />


3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-18-18-ac6d0a6a1728ff081806e5a675c63850.png" width="400" />

Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access a Spotify user's account without giving them the username or password. We'll explore OAuth more in later modules on web development, but if you want you can read more about it here: https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth

Authenticating with Spotify is quite complicated, especially when you want to access a user's account. So instead, we're going to use one of the most popular Python Spotify modules - Spotipy to make things easier.

Now that you've come so far and completed 45 days of Python, you're going to approach this challenge like a real developer, figuring things out from the documentation.



4. Using the Spotipy documentation, figure out how to authenticate your Python project with Spotify using your unique Client ID/ Client Secret.



5. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.

<img src="https://img-c.udemycdn.com/redactor/raw/article_lecture/2021-01-28_17-47-49-ca03b6a2654c0a49dcced5970d638190.png" width="400" />

<img src="https://img-c.udemycdn.com/redactor/raw/article_lecture/2021-01-28_17-44-52-1b164fc33cc35a79286a7ec0fac36f60.png" width="400" />

<img src="https://img-c.udemycdn.com/redactor/raw/article_lecture/2021-01-28_17-45-09-fbad5cf68f3a643890e33a985d69130e.png" width="400" />


HINT 1: You need your own Spotify app Client ID and Secret, the ones in the image above won't work.

HINT 2: This is the method you'll need: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth

HINT 3: Try passing the Client ID and Secret directly into the **SpotifyOAuth()** constructor instead of using `export` or `set`.

HINT 4: You need the "playlist-modify-private" scope in order to create a private playlist on Spotify.

HINT 5:  If successful, you should see the page below show up automatically (be sure to click Agree):

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-29-07-8ba3fc5c277b107461713b02e4258407.png" width="400" />

Then it will take you to the page below, example.com and you need to **copy the entire URL** in the address bar:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-32-02-17be790a8783bf4fdc4eeff77b497044.png" width="400" />


Finally, you need to paste the URL into the prompt in PyCharm:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-33-32-d74d3b92b54b2d5f4a10bdfbab4108a6.png" width="400" />

Now if you close PyCharm and restart, you should see a new file in this project called token.txt

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-35-25-694e181919606b4239d52f750c82ecde.png" width="400" />

5. Get the user id of the authenticated user (your Spotify username).

HINT 1: You'll need this method: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user

HINT 2: The output of the above method is a dictionary, look for the value of the "id" key.


## Step 3 - Search Spotify for the Songs from Step 1
1. Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).

HINT 1: You can use the query format "track: {name} year: {YYYY}" to narrow down on a track name from a particular year.

HINT 2: Sometimes a song is not available in Spotify, you'll want to use exception handling to skip over those songs.

HINT 3: `pprint()` might help you visualise the result better. https://docs.python.org/3/library/pprint.html


## Step 4 - Creating and Adding to Spotify Playlist
1. Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date you inputted in step 1.

HINT: You'll need the user id you got from Step 2.

2. Add each of the songs found in Step 3 to the new playlist.

HINT: You'll need the playlist id which is returned as an output once you've successfully created a new playlist.