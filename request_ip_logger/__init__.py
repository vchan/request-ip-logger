import grequests

TIMEOUT = 10  # seconds
URL = 'http://httpbin.org/ip'


def request_ip(proxies=None, concurrent_requests=1, timeout=TIMEOUT):
    """Make asynchronous requests to ``URL``"""
    rs = (grequests.get(URL, proxies=proxies, timeout=timeout) for i in range(concurrent_requests))
    for r in grequests.map(rs):
        if r:
            yield r.json().get('origin')
        else:
            yield None
