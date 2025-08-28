from core.client import spotify
from datetime import datetime

def get_last_album_date(artist_name):
    """
    Pega a data do último álbum do artista via Spotipy
    """
    results = spotify.sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artist_id = results['artists']['items'][0]['id']

    albums = spotify.sp.artist_albums(artist_id, album_type='album', limit=1)
    ultimo_album = albums['items'][0]
    release_date = ultimo_album['release_date']  # YYYY-MM-DD

    return datetime.fromisoformat(release_date)

def dias_desde_ultimo_album(artist_name):
    ultimo_album = get_last_album_date(artist_name)
    hoje = datetime.now()
    return (hoje - ultimo_album).days
