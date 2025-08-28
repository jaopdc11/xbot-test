from modules.get_time import dias_desde_ultimo_album
from modules.post import postar
import random

artista = 'Frank Ocean'

mensagens = [
    "Já se passaram {dias} dias desde o último álbum de {artista}. Cadê você, {artista}? 😭",
    "Frank, meu parceiro, {dias} dias sem álbum novo? Tô na saudade! 🥲",
    "Caralho, {artista}, {dias} dias e nada de álbum? Vamo agilizar! 😤",
    "Passaram {dias} dias desde o último álbum de {artista} 😢",
    "Ei, {artista}, {dias} dias sem um som novo? Tô implorando! 🙏",
    "{dias} dias sem álbum novo do {artista}. Alguém avisa pfv 🗣️",
    "{dias} dias e contando... {artista}, lança algo antes que eu desista! 😩"
]

def main():
    dias = dias_desde_ultimo_album(artista)
    tweet = random.choice(mensagens).format(dias=dias, artista=artista)
    postar(tweet)

if __name__ == '__main__':
    main()