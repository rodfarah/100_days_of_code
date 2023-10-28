from bs4 import BeautifulSoup
import requests
from decouple import config
import spotipy
from spotipy import SpotifyOAuth


SPOTIFY_CLIENT_ID = config("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URL = config("SPOTIFY_REDIRECT_URL")
SPOTIFY_DISPLAY_NAME = config("SPOTIFY_DISPLAY_NAME")
SPOTIFY_POST_INITIAL_ENDPOINT = "https://api.spotify.com/v1/playlists/"
BILLBOARD_ADRESS = "https://www.billboard.com/charts/hot-100/"

particular_date = input("Please, insert the date (YYYY-MM-DD): ")


# Scrap Billboard website:
whole_html = requests.get(url=f"{BILLBOARD_ADRESS}{particular_date}").text
billboard_soup = BeautifulSoup(whole_html, "html.parser")
hundred_songs_html = billboard_soup.select("li ul li h3")
hundred_songs_list = [song.getText().strip() for song in hundred_songs_html]

# Spotify Authentication:
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URL, scope="playlist-modify-private", show_dialog=True,
                                               cache_path="token.txt", username=SPOTIFY_DISPLAY_NAME
                                               ))
user_id = sp.current_user()["id"]

# Search Spotify for songs by title:
songs_uris = []
year = particular_date[:4]
for song in hundred_songs_list:
    result =sp.search(q=f"track:{song} year:{year}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except:
        print(f"{song} does not exist in Spotify. Skipped.")

# Create Spotify Playlist:
billboard_playlist = sp.user_playlist_create(user=user_id, public=False, name=f"100 Top from {particular_date}")

# Add songs to Playlist:
sp.user_playlist_add_tracks(user=user_id, playlist_id=billboard_playlist["id"], tracks=songs_uris)

