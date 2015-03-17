import re
import requests
from bs4 import BeautifulSoup
from time import sleep


class LinkCrawler:
    unsafeRegex = re.compile('safety/unsafe_link_warning')

    def __init__(self, link):
        self._r = requests.get(link, allow_redirects=True)

        if self.unsafeRegex.search(self._r.url):
            raise UnsafeLinkError()

        if self._r.status_code < 300:
            self._page = BeautifulSoup(self._r.text)
            self.twitter_url = link
            self.url = self._r.url

            try:
                self.title = self._page.title.text.strip()
            except:
                raise ParseLinkError()

        else:
            raise HTTPError(self._r)

    def __repr__(self):
        return '<LinkCrawler twitter_url: %s>' % self.twitter_url

class ParseLinkError(Exception):
    def __repr__(self):
        return "Parse Error: cannot retrieve webpage title"

class HTTPError(Exception):
    def __init__(self, request):
        self.r = request

    def __repr__(self):
        return "Missing Link: %s" % (self.r)

class UnsafeLinkError(Exception):
    def __repr__(self):
        return "Unsafe Link"