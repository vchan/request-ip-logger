from collections import Counter
import pprint

from request_ip_logger import request_ip

# Assuming Luminati's proxy manager is running locally
PROXIES = {
    'http': '127.0.0.1:24000',
    'https': '127.0.0.1:24000'
}


def make_requests(num_requests, concurrent_requests):
    """Make `num_requests` divided over `concurrent_requests`"""
    num_iterations = num_requests // concurrent_requests
    for i in range(num_iterations):
        yield request_ip(proxies=PROXIES, concurrent_requests=concurrent_requests)
    remainder = num_requests - (num_iterations * concurrent_requests)
    if remainder:
        yield request_ip(proxies=PROXIES, concurrent_requests=remainder)


if __name__ == '__main__':
    """Count occurrences of IPs used by Luminati"""
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('num_requests', help='total number of requests', type=int)
    parser.add_argument('concurrent_requests', help='number of requests to make concurrently', type=int)
    args = parser.parse_args()

    ip_counts = Counter()
    for r in make_requests(args.num_requests, args.concurrent_requests):
        ip_counts.update(r)
    pprint.pprint(ip_counts)
