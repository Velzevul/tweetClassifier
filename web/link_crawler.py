import re
import requests


class LinkCrawler:
    titleRegex = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)

    def __init__(self, link):
        r = requests.get(link, allow_redirects=True)

        if r.status_code < 300:
            self.r = r
            self.original_url = link
            self.url = r.url
            self.title = self.titleRegex.search(r.text).group(1).strip()
        else:
            print('Error: %s' % r.status_code)

    def __repr__(self):
        return '<LinkCrawler url: %s>' % self.url


# class LinkRetrievalProblem(Exception):
#     def __init__(self, request):
#         self.r = request