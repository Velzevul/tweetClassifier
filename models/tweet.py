from models import db, posts_tweets


class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String(255))
    entity_hashtags = db.Column(db.String(255))
    entity_urls = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)

    # relationships
    author_id = db.Column(db.BigInteger, db.ForeignKey('authors.id'))
    posts = db.relationship('Post', secondary=posts_tweets, backref=db.backref('tweets', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<tweet %s: %s >' % (self.id, self.text)
