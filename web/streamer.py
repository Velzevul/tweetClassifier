from tweepy.streaming import StreamListener
# from .link_crawler import LinkCrawler, LinkRetrievalProblem

# 438435188755161089 - id of deleted tweet (for testing purposes)

class Streamer(StreamListener):
    def __init__(self, callback):
        super(Streamer, self).__init__()
        self.store_callback = callback

    def on_status(self, status):
        if status.in_reply_to_status_id:
            print('Is a reply, skip...')
        elif len(status.entities['urls']) == 0:
            print('No links, skip...')
        else:
            print('Matching! store...')
            self.store_callback(status)


    def on_error(self, status_code):
        print("Error %s" % status_code)