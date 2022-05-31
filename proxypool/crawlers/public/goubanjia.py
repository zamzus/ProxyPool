# from proxypool.schemas.proxy import Proxy
# from proxypool.crawlers.base import BaseCrawler
# from pyquery import PyQuery
#
# BASE_URL = 'http://www.goubanjia.com/'
#
#
# class GoubanjiaCrawler(BaseCrawler):
#     """
#     ip  Goubanjia crawler, http://www.goubanjia.com/
#     """
#     urls = [BASE_URL]
#
#     def parse(self, html):
#         """
#         parse html file to get proxies
#         :return:
#         """
#         doc = PyQuery(html)
#         for td in doc('.ip').items():
#             trs = td.children()
#             ip_str = ''
#             for tr in trs:
#                 attrib = tr.attrib
#                 if 'style' in attrib and 'none' in tr.attrib['style']:
#                     continue
#                 ip_str += '' if not tr.text else tr.text
#             addr_split = ip_str.split(':')
#             if len(addr_split) == 2:
#                 host = addr_split[0]
#                 port = addr_split[1]
#                 yield Proxy(host=host, port=port)
#             else:
#                 port = trs[-1].text
#                 host = ip_str.replace(port, '')
#                 yield Proxy(host=host, port=port)
#
#
# if __name__ == '__main__':
#     crawler = GoubanjiaCrawler()
#     for proxy in crawler.crawl():
#         print(proxy)
