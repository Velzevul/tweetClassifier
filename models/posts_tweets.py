from models import db

posts_tweets = db.Table('posts_tweets',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tweet_id', db.BigInteger, db.ForeignKey('tweets.id'))
)