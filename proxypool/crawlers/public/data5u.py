# from pyquery import PyQuery
# from proxypool.schemas.proxy import Proxy
# from proxypool.crawlers.base import BaseCrawler
#
# BASE_URL = 'http://www.data5u.com/'
#
#
# class Data5UCrawler(BaseCrawler):
#     """
#     data5u crawler, http://www.data5u.com/
#     """
#     urls = [BASE_URL]
#
#     def parse(self, html):
#         """
#         parse html file to get proxies
#         :return:
#         """
#         doc = PyQuery(html)
#         for item in doc('.wlist ul.l2').items():
#             scheme = item.find('span:nth-child(4)').text()
#             host = item.find('span:first-child').text()
#             port = int(item.find('span:nth-child(2)').text())
#             if scheme.lower().find('https') > -1:
#                 yield Proxy(scheme='https', host=host, port=port)
#             yield Proxy(scheme='http', host=host, port=port)
#
#
# if __name__ == '__main__':
#     crawler = Data5UCrawler()
#     for proxy in crawler.crawl():
#         print(proxy)
