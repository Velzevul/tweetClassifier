from tweepy import OAuthHandler, Stream
from web import *
from models import *


def watch():
    consumer_key = "Z8ooyQfPan4wwQfuSigpZDJ6w"
    consumer_secret = "lYhZa0a28PH7B0tvxmTyj0xpQ9tO35HfQMapamPt3Jr8aWr6aM"
    access_token = "2204356587-6dXMm5nzMdGyRt0Z6XqCJsfTcODLSBVadbF8lEC"
    access_token_secret = "TEdGluVcdYDD7HlwT23aBcip0LpGnFp8m9xNr7dNlDKKS"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, Streamer(store_status), timeout=None)
    stream.filter(track=["photoshop"], languages=["en"])


def store_status(status):
    print("  Tweet %s" % status.id)
    tweet = Tweet(id=status.id,
                  text=status.text,
                  entity_hashtags=' '.join([ht['text'] for ht in status.entities['hashtags']]),
                  entity_urls=' '.join([url['url'] for url in status.entities['urls']]),
                  created_at=status.created_at)

    author = Author.query.get(status.author.id)
    if not author:
        author = Author(id=status.author.id, name=status.author.screen_name)

    posts = []
    for url in status.entities['urls']:
        twitter_url = url['url']

        post = Post.query.filter_by(twitter_url=twitter_url).first()

        if not post:
            post = Post(twitter_url=twitter_url)

        try:
            crawled_url = LinkCrawler(twitter_url)
            post.url = crawled_url.url
            post.title = crawled_url.title
        except Exception as err:
            # link is broken, repoxrted, or cannot be parsed
            print(err)
            post.error_description = repr(err)

        posts.append(post)

    tweet.posts.extend(posts)
    author.tweets.append(tweet)

    models.db.session().add(tweet)

    try:
        print('  saving...')
        models.db.session().commit()
        print('  >> Success:')
        print('       text: %s' % tweet.text)
        print('       author: %s' % author.name)
        print('       posts:')
        for post in posts:
            print('         %s' % post.original_url)
        return True
    except Exception as e:
        print("  >> Error: %s" % e)
        models.db.session().rollback()
        return False


if __name__ == '__main__':
    watch()