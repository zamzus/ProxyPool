from proxypool.schemas import Proxy


def is_valid_proxy(data):
    """
    check this string is within proxy format
    """
    if data.__contains__(':'):
        ip, port = data.split('://')[-1].split(':')
        return is_ip_valid(ip) and is_port_valid(port)
    else:
        return is_ip_valid(data)


def is_ip_valid(ip):
    """
    check this string is within ip format
    """
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def is_port_valid(port):
    return port.isdigit()


def convert_proxy_or_proxies(data):
    """
    convert list of str to valid proxies or proxy
    :param data:
    :return:
    """
    if not data:
        return None
    # if list of proxies
    if isinstance(data, list):
        result = []
        for item in data:
            # skip invalid item
            item = item.strip()
            if not is_valid_proxy(item):
                continue
            scheme = item.split('://')[0]
            host, port = item.split('://')[-1].split(':')
            result.append(Proxy(scheme=scheme, host=host, port=int(port)))
        return result
    if isinstance(data, str) and is_valid_proxy(data):
        scheme = data.split('://')[0]
        host, port = data.split('://')[-1].split(':')
        return Proxy(scheme=scheme, host=host, port=int(port))
