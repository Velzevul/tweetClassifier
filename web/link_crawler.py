from bs4 import BeautifulSoup
import requests

class LinkCrawler:
    def __init__(self, link):
        r = requests.get(link, allow_redirects = True)

        if r.status < 300:
            self.short_url = link
            self.full_url = self.r.url
            self.page = BeautifulSoup(self.r.text)
        else:


    def __repr__(self):
        return '<LinkCrawler url: %s>' % self.short_url

class LinkRetrievalProblem(Exception):
    def __init__(self, request):
        self.r = request