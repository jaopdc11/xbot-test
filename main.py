from modules.get_time import dias_desde_ultimo_album
from modules.post import postar
import random

artista = 'Frank Ocean'

def main():
    dias = dias_desde_ultimo_album(artista)
    messages = [
        f'Já se passaram {dias} dias desde o lançamento do último álbum de {artista}.',
        f'{artista} sumiu há {dias} dias...',
        f'Po, {artista}, {dias} dias sem álbum... Vamo trabalhar {artista[0]} 😭'
    ]
    tweet = random.choice(messages)
    postar(tweet)

if __name__ == '__main__':
    main()
