# coding=utf-8
from data_collection.html_downLoad import HtmlDownLoader
from data_collection.html_output import HtmlOutPuter
from data_collection.html_parse import HtmlParser
from data_collection.url_manager import UrlManager


class Spidermain(object):

    def __init__(self):
        self.urls = UrlManager()
        self.downLoader = HtmlDownLoader()
        self.parser = HtmlParser()
        self.outputData = HtmlOutPuter()

    def craw(self, root_url):
        count = 0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print(new_url)
                html_data = self.downLoader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_data)
                self.urls.add_new_urls(new_urls)
                self.outputData.collect_data(new_data)
                count += 1
                print(count)
            except Exception as e:
                print(Exception,":",e)
                print("craw failed")


        self.outputData.output_text()


if __name__ == "__main__":
    root_url = "https://movie.douban.com/subject/26862829/comments?sort=new_score&status=P"
    obj_spider = Spidermain()
    obj_spider.craw(root_url)

