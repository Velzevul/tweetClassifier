from app import db, Link
from web.link_crawler import LinkCrawler

def fix_links(force = False):
    links = Link.query.all()

    for link in links:
        if not link.title  or force:
            print('fixing link %s' % link)

            crawler = LinkCrawler(link.shortened_url)
            link.url = crawler.full_url
            # print(crawler.page.text)
            # print(crawler.page.find('title'))
            # print(crawler.page.text)
            # print(crawler.page.find('title'))
            link.title = crawler.page.find('title').text.strip()

            db.session.add(link)
            db.session.commit()

if __name__ == '__main__':
    fix_links()