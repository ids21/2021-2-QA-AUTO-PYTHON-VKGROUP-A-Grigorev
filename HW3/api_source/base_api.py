import pytest

from utils.builder import Builder
from api_source.client import  ApiClient


class ApiBase:
    authorize = True
    publish = True
    blog_id = 378

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, logger):
        self.api_client: ApiClient = api_client
        self.builder = Builder()
        self.logger = logger

        if self.authorize:
            self.api_client.post_login()