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
        messages = [
            f'Já se passaram {dias} dias desde o lançamento do último álbum de {artista}.',
            f'{artista} sumiu há {dias} dias...',
            f'Po, {artista}, {dias} dias sem álbum... Vamo trabalhar {artista[0]} 😭'
        ]
        tweet = random.choice(messages)
        postar(tweet)
        return {"status": "ok", "tweet": tweet}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
