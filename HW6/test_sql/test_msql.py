from test_sql.base import MysqlBase
from utils import anlyzer
from models.model import (
    CountRequest, 
    RequestTypeCount, 
    MostFrequentRequest, 
    Largest4xxRequest, 
    UserWith5xxRequests
)


class TestRequestsCount(MysqlBase):

    def prepare(self):
        req_count = anlyzer.count_requests()
        self.count_records = self.get_count_records(model=CountRequest)
        self.mysql_builder.create_requests_count(req_count)

    def test_did_request_count_added(self):
        after_count = self.get_count_records(model=CountRequest)
        assert self.count_records != after_count, (
            f"Error occured after insert data: {self.count_records} != {after_count}"
        )

class TestRequestTypesCount(MysqlBase):

    def prepare(self):
        req_types_count = anlyzer.count_request_types()
        self.count_records = self.get_count_records(model=RequestTypeCount)
        for req_type in req_types_count:
            self.mysql_builder.create_request_type_count(
                req_type=req_type[0], 
                count=req_type[1]
            )
    def test_most_did_request_type_count_info_added(self):
        after_count = self.get_count_records(model=RequestTypeCount)
        assert self.count_records != after_count, (
            f"Error occured after insert data: {self.count_records} != {after_count}"
        )


class TestMostFrequentRequests(MysqlBase):

    def prepare(self):
        most_freq_reqs = anlyzer.most_frequent_requests()
        self.count_records = self.get_count_records(model=MostFrequentRequest)
        for most_freq_req in most_freq_reqs:
            self.mysql_builder.create_most_frequent_request(
                url=most_freq_req[0], 
                count=most_freq_req[1]
            )

    def test_most_did_most_frequent_request_info_added(self):
        after_count = self.get_count_records(model=MostFrequentRequest)
        assert self.count_records != after_count, (
            f"Error occured after insert data: {self.count_records} != {after_count}"
        )
        
    


class TestLargest4xxRequests(MysqlBase):

    def prepare(self):
        largest_4xx_reqs = anlyzer.largest_4xx_requests()
        self.count_records = self.get_count_records(model=Largest4xxRequest)
        for req in largest_4xx_reqs:
            self.mysql_builder.create_largest_4xx_request(
                url=req[0], 
                size=req[1], 
                ip=req[2]
            )
    def test_most_did_largest_4xx_requests_info_added(self):
        after_count = self.get_count_records(model=Largest4xxRequest)
        assert self.count_records != after_count, (
            f"Error occured after insert data: {self.count_records} != {after_count}"
        )
    



class TestUsersWith5xxRequests(MysqlBase):

    def prepare(self):
        users_with_5xx_reqs = anlyzer.users_with_5xx_requests()
        self.count_records = self.get_count_records(model=UserWith5xxRequests)
        for user in users_with_5xx_reqs:
            self.mysql_builder.create_user_with_5xx_requests(
                ip=user[0], 
                requests_number=user[1]
            )

    def test_most_did_users_with_5xx_reqs_info_added(self):
        after_count = self.get_count_records(model=UserWith5xxRequests)
        assert self.count_records != after_count, (
            f"Error occured after insert data: {self.count_records} != {after_count}"
        )
