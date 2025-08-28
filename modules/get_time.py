from core.client import spotify
from datetime import datetime
import os

base_dir = os.path.dirname(__file__)
data_file = os.path.join(base_dir, "etc", "secrets", "data.txt")

def get_last_album_date(artist_name):
    results = spotify.sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artist_id = results['artists']['items'][0]['id']

    albums = spotify.sp.artist_albums(artist_id, album_type='album', limit=1)
    ultimo_album = albums['items'][0]
    release_date = ultimo_album['release_date']
    return datetime.fromisoformat(release_date)

def dias_desde_ultimo_album(artist_name):
    ultimo_album = get_last_album_date(artist_name)
    hoje = datetime.now()
    return (hoje - ultimo_album).days

def dias_atuais_e_verifica(artist_name):
    dias_atual = dias_desde_ultimo_album(artist_name)

    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            try:
                dias_ultimo = int(f.read().strip())
            except ValueError:
                dias_ultimo = None
    else:
        dias_ultimo = None

    if dias_ultimo != dias_atual:
        with open(data_file, "w", encoding="utf-8") as f:
            f.write(str(dias_atual))
        return dias_atual
    else:
        return None
