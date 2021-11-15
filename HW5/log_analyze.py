import os
import json
from collections import Counter

LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'access.log'))
RES_FILE_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'HW5', 'python_results.json'))
JSON_DATA = {}


def count_requests():
    with open(LOG_FILE, 'r') as log:
        all_requests_count = len(log.readlines())

    JSON_DATA.setdefault('all_requests_count', all_requests_count)
    json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)


def count_request_types():
    with open(LOG_FILE, 'r') as log:
        req_type_column = [req.split()[5][1:] for req in log.readlines()]
        req_types = Counter(req_type_column).most_common()

    count_req_types = {req[0]: req[1] for req in req_types}
    JSON_DATA.setdefault('Count_of_requests_by_type', count_req_types)
    json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)


def most_frequent_requests():
    with open(LOG_FILE, 'r') as log:
        url_column = [req.split()[6] for req in log.readlines()]
        freq_requests = Counter(url_column).most_common(10)

    most_freq_reqs = {i+1: {'URL': req[0], 'Number_of_requests': req[1]}
                    for i, req in zip(range(len(freq_requests)), freq_requests)}
    JSON_DATA.setdefault('Top_10_most_frequent_requests', most_freq_reqs)
    json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)


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

    largest_reqs = {i+1: {'URL': req[0], 'Response_code': req[1], 'Size': req[2], 'IP': req[3]}
                    for i, req in zip(range(len(data)), data[:5])}
    JSON_DATA.setdefault('Top_5_largest_requests_with_4xx_error', largest_reqs)
    json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)


def users_with_5xx_requests():
    with open(LOG_FILE, 'r') as log:
        ip_with_5xx = []
        for _request in log.readlines():
            if (int(_request.split()[8]) >= 500 and int(_request.split()[8])<600):
                ip_with_5xx.append(_request.split()[0])
        freq_ip = Counter(ip_with_5xx).most_common(5)

    users_with_5xx = {i+1: {'IP': ip[0], 'Number_of_requests': ip[1]}
                        for i, ip in zip(range(len(freq_ip)), freq_ip)}
    JSON_DATA.setdefault('Top_5_users_by_the_requests_with_5xx_erorr', users_with_5xx)
    json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)


if __name__== "__main__":
    count_requests()
    count_request_types()
    most_frequent_requests()
    largest_4xx_requests()
    users_with_5xx_requests()