import pytest

from utils.builder import Builder
from api_source.client import  ApiClient


class ApiBase:
    authorize = True
    api_client: ApiClient = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client: ApiClient, logger):
        self.api_client = api_client
        self.builder = Builder()
        self.logger = logger

        if self.authorize:
            self.api_client.post_login()