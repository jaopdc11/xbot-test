from core.client import x

def postar(tweet):
    try:
        x.client.create_tweet(text=tweet)
        print("Postado:", tweet)
    except Exception as e:
        print("Erro ao postar:", e)