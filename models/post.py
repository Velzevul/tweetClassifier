from models import db, posts_tweets


class Post(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    twitter_url = db.Column(db.String(255), unique=True)
    url = db.Column(db.Text)
    title = db.Column(db.String(255))
    error_description = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s: %s >' % (self.id, self.twitter_url)
