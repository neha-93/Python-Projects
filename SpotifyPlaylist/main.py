import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "693263f74da94e1c86e54198cf17275f"
CLIENT_SECRET = "dacd5b77129f4c26a96e0b80f2c080b4"
REDIRECT_URI = "http://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=f"{URL}{date}")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

all_songs = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song "
                                                                          "text--truncate color--primary")]

all_artist = [artist.getText() for artist in soup.find_all(name="span", class_="chart-element__information__artist"
                                                                               " text--truncate color--secondary")]

print(all_songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

uri_list = []

for i in range(len(all_songs)):
    searchQuery = all_songs[i] + ' ' + all_artist[i]
    searchResults = sp.search(q=searchQuery, limit=1)
    try:
        current_uri = searchResults["tracks"]["items"][0]["uri"]
        uri_list.append(current_uri)
    except IndexError:
        pass

print(uri_list)

new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False,
                                       description="A playlist that takes you back in time!")

playlist_id = new_playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
