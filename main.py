from modules.get_time import dias_desde_ultimo_album
from modules.post import postar

artista = 'Frank Ocean'

def main():
    dias = dias_desde_ultimo_album(artista)
    tweet = f'Já se passaram {dias} dias desde o último álbum de {artista}.'
    postar(tweet)

if __name__ == '__main__':
    main()
