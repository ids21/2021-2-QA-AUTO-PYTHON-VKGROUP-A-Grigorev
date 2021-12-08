import os
from collections import Counter

LOG_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 
    os.pardir, 
    'access.log')
)


def count_requests():
    with open(LOG_FILE, 'r') as log:
        all_requests_count = len(log.readlines())
    return all_requests_count


VALID_REQUESTS = ['PUT', 'DELETE', 'GET', 'POST', 'HEAD']

def count_request_types():
    with open(LOG_FILE, 'r') as log:
        request_by_type = [req.split()[5][1:] for req in log.readlines()]
        req_types = dict(Counter(request_by_type).most_common())
        for key, value in req_types.items():
            if key not in VALID_REQUESTS:
                req_types['INVALID_REQUEST'] = req_types.pop(key)
                

    return req_types


def most_frequent_requests(count_most_common:int= 10):
    with open(LOG_FILE, 'r') as log:
        url_column = [req.split()[6] for req in log.readlines()]
        freq_requests = Counter(url_column).most_common(count_most_common)

    return freq_requests

def largest_4xx_requests():
    with open(LOG_FILE, 'r') as log:
        data = []
        for _request in log.readlines():
            if (int(_request.split()[8]) >= 400 and int(_request.split()[8])<500):
                data.append((
                    _request.split()[6], 
                    int(_request.split()[8]), 
                    int(_request.split()[9]), 
                    _request.split()[0]
                ))

        data.sort(key=lambda req: req[2], reverse=True)
        return data[:5]


def users_with_5xx_requests():
    with open(LOG_FILE, 'r') as log:
        ip_5xx_errors = []
        for _request in log.readlines():
            if (int(_request.split()[8]) >= 500 and int(_request.split()[8])<600):
                ip_5xx_errors.append(_request.split()[0])
        top_five_ip = Counter(ip_5xx_errors).most_common(5)
    return top_five_ip