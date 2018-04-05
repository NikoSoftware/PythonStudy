# coding=utf-8
import ssl
from urllib import request


class HtmlDownLoader(object):
    def download(self, url):
        if url is None:
            return None
        ssl._create_default_https_context = ssl._create_unverified_context
        response = request.urlopen(url)
        return response.read()

