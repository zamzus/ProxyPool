import re
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

MAX_NUM = 99
BASE_URL = 'http://api.89ip.cn/tqdl.html?api=1&num={MAX_NUM}&port=&address=&isp='.format(MAX_NUM=MAX_NUM)


class Ip89Crawler(BaseCrawler):
    """
    89ip crawler, http://api.89ip.cn
    """
    urls = [BASE_URL]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        host_port_ls = re.findall('((?:\d+.?)+):(\d+).*?<br>', html)
        for host, port in host_port_ls:
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = Ip89Crawler()
    for proxy in crawler.crawl():
        print(proxy)
