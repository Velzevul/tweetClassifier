from tweepy.streaming import StreamListener
import models
# from .link_crawler import LinkCrawler, LinkRetrievalProblem

# 438435188755161089 - id of deleted tweet (for testing purposes)

class Streamer(StreamListener):
    def on_status(self, status):
        if status.in_reply_to_status_id:
            print('Is a reply, skip...')
        elif len(status.entities['urls']) == 0:
            print('No links, skip...')
        else:
            print('Matching! store...')
            store_status(status)


    def on_error(self, status_code):
        print("Error %s" % status_code)


def store_status(status):
    print("  Tweet %s" % status.id)
    tweet = models.Tweet(id=status.id,
                         text=status.text,
                         entity_hashtags=' '.join([ht['text'] for ht in status.entities['hashtags']]),
                         entity_urls=' '.join([url['expanded_url'] for url in status.entities['urls']]),
                         created_at=status.created_at)

    author = models.Author.query.get(status.author.id)
    if not author:
        author = models.Author(id=status.author.id, name=status.author.screen_name)

    posts = []
    for url in status.entities['urls']:
        post = models.Post.query.filter_by(url=url['expanded_url']).first()

        if not post:
            pass
            # classify post here based on learnt model
            # expanded_url = LinkCrawler(url)
            # post = models.Post(original_url=expanded_url.original_url, url=expanded_url.url, title=expanded_url.title)

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
