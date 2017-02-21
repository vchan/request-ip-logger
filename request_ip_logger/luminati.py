from collections import Counter
import pprint

from request_ip_logger import request_ip

# Assuming Luminati's proxy manager is running locally
PROXIES = {
    'http': '127.0.0.1:24000',
    'https': '127.0.0.1:24000'
}


if __name__ == '__main__':
    # Count occurrences of IPs used by Luminati in 100 requests
    ip_counts = Counter()
    for i in range(10):
        ip_counts.update(request_ip(proxies=PROXIES, concurrent_requests=10))
    pprint.pprint(ip_counts)
