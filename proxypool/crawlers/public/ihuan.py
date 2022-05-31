import re
import time
# from pyquery import PyQuery
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'https://ip.ihuan.me/today/{path}.html'


class IhuanCrawler(BaseCrawler):
    """
    ip ihuan crawler, https://ip.ihuan.me/
    """
    path = time.strftime("%Y/%m/%d/%H", time.localtime())
    urls = [BASE_URL.format(path=path)]
    ignore = False

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        host_port_scheme_other_ls = re.findall('((?:\d+.?)+):(\d+)@(\w+)(.*?)<br>', html)
        for host, port, scheme, other in host_port_scheme_other_ls:
            if other.lower().find('https') > -1:
                scheme = 'https'
            yield Proxy(scheme=scheme.lower(), host=host, port=port)
            if scheme.lower() == 'https':
                yield Proxy(scheme='http', host=host, port=port)


if __name__ == '__main__':
    crawler = IhuanCrawler()
    for proxy in crawler.crawl():
        print(proxy)
