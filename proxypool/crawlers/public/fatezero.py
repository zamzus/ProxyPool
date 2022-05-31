from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import json

BASE_URL = 'http://proxylist.fatezero.org/proxy.list'


class FatezeroCrawler(BaseCrawler):
    """
    Fatezero crawler, http://proxylist.fatezero.org/
    """
    urls = [BASE_URL]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        proxyinfo_ls = html.split('\n')
        for proxyinfo in proxyinfo_ls:
            if not proxyinfo:
                continue
            proxyinfo = json.loads(proxyinfo)
            if proxyinfo.get('country') and proxyinfo['country'].lower() != 'cn':
                continue
            scheme = proxyinfo['type'].lower()
            host = proxyinfo['host']
            port = proxyinfo['port']
            yield Proxy(scheme=scheme, host=host, port=port)
            if scheme == 'https':
                yield Proxy(scheme='http', host=host, port=port)


if __name__ == '__main__':
    crawler = FatezeroCrawler()
    for proxy in crawler.crawl():
        print(proxy)
