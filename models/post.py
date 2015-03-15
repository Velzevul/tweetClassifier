from models import db, posts_tweets


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255))
    title = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s: %s >' % (self.id, self.original_url)
