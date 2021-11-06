import pytest
import allure

from exceptions.exceptions import InvalidLoginException
from api_source.base_api import ApiBase

@allure.epic("API")
@allure.feature("Authorization")
class TestApi(ApiBase):
    authorize = False

    @allure.story("Valid login")
    @pytest.mark.API
    def test_valid_login(self):
        pass