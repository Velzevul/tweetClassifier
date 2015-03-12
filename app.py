from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://soft_info:@localhost/soft_info'
db = SQLAlchemy(app)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortened_url = db.Column(db.String(50), unique = True)
    url = db.Column(db.String(255) , unique = True)
    host_id = db.Column(db.Integer)
    tweets_count = db.Column(db.Integer)
    title = db.Column(db.String(255))

    def __init__(self, shortened_url):
        self.shortened_url = shortened_url

    def __repr__(self):
        return '<Link %s --> %s >' % (self.shortened_url, self.url)
