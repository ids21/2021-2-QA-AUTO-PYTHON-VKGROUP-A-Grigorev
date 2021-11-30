import os
import json
from collections import Counter

LOG_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 
    os.pardir, 
    'access.log')
)
RESULT_JSON = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 
    os.pardir, 
    'HW5', 
    'python_results.json')
)
RESULT_TXT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 
    os.pardir, 
    'HW5', 
    'python_results.txt')
)
JSON_RESULT_DATA = {}


def count_requests(json_file = False):
    with open(LOG_FILE, 'r') as log:
        all_requests_count = len(log.readlines())
    if json_file:
        JSON_RESULT_DATA.setdefault('all_requests_count', all_requests_count)
        json.dump(JSON_RESULT_DATA, open(RESULT_JSON, 'w'), indent=4)
    else:
        with open(RESULT_TXT, 'w') as log_result:
            log_result.writelines(['All requests count: %s \n' % str(all_requests_count)])



def count_request_types(json_file = False):
    with open(LOG_FILE, 'r') as log:
        request_by_type = [req.split()[5][1:] for req in log.readlines()]
        req_types = Counter(request_by_type).most_common()

    if json_file:
        count_req_types = {req[0]: req[1] for req in req_types}
        JSON_RESULT_DATA.setdefault('Count_of_requests_by_type', count_req_types)
        json.dump(JSON_RESULT_DATA, open(RESULT_JSON, 'w'), indent=4)
    else:
        with open(RESULT_TXT, 'a') as log_result:
            log_result.write('\nCount of requests by HTTP method \n')
            log_result.writelines(["Method:%s Count:%s\n" % (req[1],req[0]) for req in req_types])


def most_frequent_requests(json_file = False):
    with open(LOG_FILE, 'r') as log:
        url_column = [req.split()[6] for req in log.readlines()]
        freq_requests = Counter(url_column).most_common(10)

    if json_file:
        most_freq_reqs = {i+1: {'URL': req[0], 'Number_of_requests': req[1]}
                    for i, req in zip(range(len(freq_requests)), freq_requests)}

        JSON_RESULT_DATA.setdefault('Top_10_most_frequent_requests', most_freq_reqs)
        json.dump(JSON_RESULT_DATA, open(RESULT_JSON, 'w'), indent=4)
    else:
        with open(RESULT_TXT, 'a') as log_result:
            log_result.write('\n TOP-10 most frequent requsts: \n')
            log_result.writelines(['url: %s count: %s \n' % (req[0], req[1]) for req in freq_requests])


def largest_4xx_requests(json_file = False):
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
    if json_file:
        largest_reqs = {i+1: {'URL': req[0], 'Response_code': req[1], 'Size': req[2], 'IP': req[3]}
                    for i, req in zip(range(len(data)), data[:5])}
        JSON_RESULT_DATA.setdefault('Top_5_largest_requests_with_4xx_error', largest_reqs)
        json.dump(JSON_RESULT_DATA, open(RESULT_JSON, 'w'), indent=4)
    else:
        with open(RESULT_TXT, 'a') as log_result:
            log_result.write('\n TOP -5 largest requests that failed wilth (4XX) error: \n')
            log_result.writelines(
                ['URL: %s - STATUS:%s - SIZE:%s - IP:%s \n' % (req[0],req[1],req[2],req[3]) for req in data[:5]]
            )


def users_with_5xx_requests(json_file = False):
    with open(LOG_FILE, 'r') as log:
        ip_5xx_errors = []
        for _request in log.readlines():
            if (int(_request.split()[8]) >= 500 and int(_request.split()[8])<600):
                ip_5xx_errors.append(_request.split()[0])
        top_five_ip = Counter(ip_5xx_errors).most_common(5)

    if json_file:
        users_with_5xx = {i+1: {'IP': ip[0], 'Number_of_requests': ip[1]}
                        for i, ip in zip(range(len(top_five_ip)), top_five_ip)}
        JSON_RESULT_DATA.setdefault('Top_5_users_by_the_requests_with_5xx_erorr', users_with_5xx)
        json.dump(JSON_RESULT_DATA, open(RESULT_JSON, 'w'), indent=4)
    else:
        with open(RESULT_TXT, 'a') as log_result:
            log_result.write('\n Top 5 users by the number of requests that ended with a server error: \n')
            log_result.writelines(
                ['IP: %s - COUNT:%s\n' % (res[0],res[1]) for res in top_five_ip]
            )


if __name__== "__main__":
    count_requests(True)
    count_request_types(True)
    most_frequent_requests(True)
    largest_4xx_requests(True)
    users_with_5xx_requests(True)