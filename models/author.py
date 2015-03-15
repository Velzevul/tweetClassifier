from models import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<author %s: %s >' % (self.id, self.name)

