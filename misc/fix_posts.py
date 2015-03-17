from models import *
from web.link_crawler import LinkCrawler

def fix_posts(force=False):
    posts = Post.query.all()

    for post in posts:
        if not post.title or force:
            print('fixing post %s' % post)
            post.url = None
            post.title = None

            try:
                crawler = LinkCrawler(post.twitter_url)
                post.url = crawler.url
                post.title = crawler.title

            except Exception as err:
                print(err)
                post.error_description = repr(err)

            db.session.add(post)
            db.session.commit()

if __name__ == '__main__':
    fix_posts()