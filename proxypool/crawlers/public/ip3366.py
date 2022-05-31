from pyquery import PyQuery
from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'http://www.ip3366.net/free/?stype=1&page={page}'


class IP3366Crawler(BaseCrawler):
    """
    ip3366 crawler, http://www.ip3366.net/
    """
    urls = [BASE_URL.format(page=i) for i in range(1, 5)]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = PyQuery(html)
        for item in doc('table tbody tr').items():
            scheme = item.find('td:nth-child(4)').text().lower()
            host = item.find('td:nth-child(1)').text()
            port = item.find('td:nth-child(2)').text()
            yield Proxy(scheme=scheme, host=host, port=port)
            if scheme == 'https':
                yield Proxy(scheme='http', host=host, port=port)


if __name__ == '__main__':
    crawler = IP3366Crawler()
    for proxy in crawler.crawl():
        print(proxy)
