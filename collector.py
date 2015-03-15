from tweepy import OAuthHandler, Stream
from web import Streamer


def watch():
    consumer_key = "Z8ooyQfPan4wwQfuSigpZDJ6w"
    consumer_secret = "lYhZa0a28PH7B0tvxmTyj0xpQ9tO35HfQMapamPt3Jr8aWr6aM"
    access_token = "2204356587-6dXMm5nzMdGyRt0Z6XqCJsfTcODLSBVadbF8lEC"
    access_token_secret = "TEdGluVcdYDD7HlwT23aBcip0LpGnFp8m9xNr7dNlDKKS"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, Streamer(), timeout=None)
    stream.filter(track=["photoshop"], languages=["en"])

if __name__ == '__main__':
    watch()