from fastapi import FastAPI, HTTPException
from modules.get_time import dias_desde_ultimo_album
from modules.post import postar
import random

app = FastAPI()
artista = 'Frank Ocean'

@app.get("/post")
def postar_tweet():
    try:
        dias = dias_desde_ultimo_album(artista)
        primeiro_nome = artista.split(" ")[0].strip()
        messages = [
            f'Já se passaram {dias} dias desde o lançamento do último álbum de {artista}.',
            f'{artista} sumiu há {dias} dias...',
            f'Po, {artista}, {dias} dias sem álbum... Vamo trabalhar {primeiro_nome} 😭',
            f'E aí {primeiro_nome}, cadê o novo som? Já se passaram {dias} dias!',
            f'{primeiro_nome}, a galera tá esperando por mais música há {dias} dias!',
            f'Caraca, {dias} dias se foram e nada de novo do {artista}... Bora acelerar aí {primeiro_nome}!',
            f'Galera, já faz {dias} dias desde o último álbum de {artista} 😱',
            f'{primeiro_nome}, a paciência tá acabando... {dias} dias sem lançar nada!'
        ]
        tweet = random.choice(messages)
        postar(tweet)
        return {"status": "ok", "tweet": tweet}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
