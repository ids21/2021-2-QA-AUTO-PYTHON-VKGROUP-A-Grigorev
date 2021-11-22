from test_sql.base import MysqlBase
from utils import anlyzer


class TestRequestsCount(MysqlBase):

    def prepare(self):
        req_count = anlyzer.count_requests()
        self.mysql_builder.create_requests_count(req_count)


class TestRequestTypesCount(MysqlBase):

    def prepare(self):
        req_types_count = anlyzer.count_request_types()
        for req_type in req_types_count:
            self.mysql_builder.create_request_type_count(
                req_type=req_type[0], 
                count=req_type[1]
            )


class TestMostFrequentRequests(MysqlBase):

    def prepare(self):
        most_freq_reqs = anlyzer.most_frequent_requests()
        for most_freq_req in most_freq_reqs:
            self.mysql_builder.create_most_frequent_request(
                url=most_freq_req[0], 
                count=most_freq_req[1]
            )


class TestLargest4xxRequests(MysqlBase):

    def prepare(self):
        largest_4xx_reqs = anlyzer.largest_4xx_requests()
        for req in largest_4xx_reqs:
            self.mysql_builder.create_largest_4xx_request(
                url=req[0], 
                size=req[1], 
                ip=req[2]
            )



class TestUsersWith5xxRequests(MysqlBase):

    def prepare(self):
        users_with_5xx_reqs = anlyzer.users_with_5xx_requests()
        for user in users_with_5xx_reqs:
            self.mysql_builder.create_user_with_5xx_requests(
                ip=user[0], 
                requests_number=user[1]
            )
