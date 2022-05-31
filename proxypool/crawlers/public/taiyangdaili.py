from pyquery import PyQuery
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.taiyanghttp.com/free/page{num}'


class TaiyangdailiCrawler(BaseCrawler):
    """
    taiyangdaili crawler, http://www.taiyanghttp.com/free/
    """
    urls = [BASE_URL.format(num=i) for i in range(1, 6)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = PyQuery(html)
        for node in doc('#ip_list .tr.ip_tr').items():
            scheme = node.find('div:nth-child(6)').text().lower()
            host = node.find('div:nth-child(1)').text()
            port = node.find('div:nth-child(2)').text()
            yield Proxy(scheme=scheme, host=host, port=port)
            if scheme == 'https':
                yield Proxy(scheme='http', host=host, port=port)


if __name__ == '__main__':
    crawler = TaiyangdailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
