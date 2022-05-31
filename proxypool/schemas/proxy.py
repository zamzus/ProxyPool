from attr import attrs, attr


@attrs
class Proxy(object):
    """
    proxy schema
    """
    scheme = attr(type=str, default='http')
    host = attr(type=str, default=None)
    port = attr(type=int, default=None)
    
    def __str__(self):
        """
        to string, for print
        :return:
        """
        return f'{self.scheme}://{self.host}:{self.port}'
    
    def string(self):
        """
        to string
        :return: <type>://<host>:<port>
        """
        return self.__str__()


if __name__ == '__main__':
    proxy = Proxy(scheme='https', host='8.8.8.8', port=8888)
    print('proxy', proxy)
    print('proxy', proxy.string())
