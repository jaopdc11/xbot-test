import os
from dotenv import load_dotenv
import tweepy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ---------- Paths absolutos dos envs (Secret Files do Render) ----------
x_env_file = "/etc/secrets/x.env"
spotipy_env_file = "/etc/secrets/spotipy.env"

# ---------- X Client ----------
class XClient:
    def __init__(self):
        load_dotenv(x_env_file)

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_KEY_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_secret = os.getenv("ACCESS_TOKEN_SECRET")

        if not all([api_key, api_secret, access_token, access_secret]):
            raise ValueError("Alguma variável do X env não encontrada!")

        # Usar tweepy.Client para API v2
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret
        )

# ---------- Spotipy Client ----------
class SpotipyClient:
    def __init__(self):
        load_dotenv(spotipy_env_file)

        client_id = os.getenv("SPOTIPY_CLIENT_ID")
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

        if not client_id or not client_secret:
            raise ValueError("SPOTIPY_CLIENT_ID ou SPOTIPY_CLIENT_SECRET não encontrado no .env")

        os.environ["SPOTIPY_CLIENT_ID"] = client_id
        os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# ---------- Instâncias globais ----------
spotify = SpotipyClient()
x = XClient()
