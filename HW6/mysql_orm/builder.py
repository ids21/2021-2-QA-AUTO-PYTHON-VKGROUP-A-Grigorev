from models.model import CountRequest, RequestTypeCount, MostFrequentRequest, Largest4xxRequest, UserWith5xxRequests


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_requests_count(self, count):
        req_count = CountRequest(count=count)
        self.client.session.add(req_count)
        self.client.session.commit()
        return req_count

    def create_request_type_count(self, req_type, count):
        req_type_count = RequestTypeCount(req_type=req_type, count=count)
        self.client.session.add(req_type_count)
        self.client.session.commit()
        return req_type_count

    def create_most_frequent_request(self, url, count):
        most_freq_req = MostFrequentRequest(url=url, count=count)
        self.client.session.add(most_freq_req)
        self.client.session.commit()
        return most_freq_req

    def create_largest_4xx_request(self, url, size, ip):
        largest_4xx_req = Largest4xxRequest(url=url, size=size, ip=ip)
        self.client.session.add(largest_4xx_req)
        self.client.session.commit()
        return largest_4xx_req

    def create_user_with_5xx_requests(self, ip, requests_number):
        user_with_5xx_reqs = UserWith5xxRequests(ip=ip, requests_number=requests_number)
        self.client.session.add(user_with_5xx_reqs)
        self.client.session.commit()
        return user_with_5xx_reqs