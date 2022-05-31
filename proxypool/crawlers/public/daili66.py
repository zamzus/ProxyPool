from pyquery import PyQuery
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.66ip.cn/{page}.html'
MAX_PAGE = 3


class Ip66Crawler(BaseCrawler):
    """
    Ip66 crawler, http://www.66ip.cn/1.html
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = PyQuery(html)
        for tr in doc('.containerbox table tr:gt(0)').items():
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(scheme='http', host=host, port=port)
            yield Proxy(scheme='https', host=host, port=port)


if __name__ == '__main__':
    crawler = Ip66Crawler()
    for proxy in crawler.crawl():
        print(proxy)
