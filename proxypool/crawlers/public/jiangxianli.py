import json
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

MAX_PAGE = 3
BASE_URL = 'https://ip.jiangxianli.com/api/proxy_ips?page={page}'


class JiangxianliCrawler(BaseCrawler):
    """
    jiangxianli crawler, https://ip.jiangxianli.com/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        result = json.loads(html)
        if result['code'] != 0:
            return
        for node in result['data']['data']:
            if not node:
                continue
            if node['country'] != '中国':
                continue
            yield Proxy(scheme=node['protocol'].lower(), host=node['ip'], port=node['port'])
            if node['protocol'].lower() == 'https':
                yield Proxy(scheme='http', host=node['ip'], port=node['port'])


if __name__ == '__main__':
    crawler = JiangxianliCrawler()
    for proxy in crawler.crawl():
        print(proxy)
