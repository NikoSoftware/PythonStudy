# coding=utf-8
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from data_collection.html_output import HtmlOutPuter


class HtmlParser(object):
    def parse(self, page_url, html_data):
        if page_url is None and html_data is None:
            print("空数据")
            return
        soup = BeautifulSoup(html_data, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all("a", attrs={"class": "next"})
        print(links)
        print(len(links))
        for link in links:
            new_url = link["href"]
            new_full_url = urljoin("https://movie.douban.com/subject/26862829/comments", new_url)
            print(new_full_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = set()
        comments = soup.find_all("p", _class="")
      #  print(movies)
        for comment in comments:
            res_data.add(str(comment.string))

        return res_data
