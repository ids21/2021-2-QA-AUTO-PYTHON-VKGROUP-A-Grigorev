from source.main.main_page import MainPage
from base import BaseCase

import allure
import pytest


@allure.epic("Main Page")
@allure.feature("Authorization")
class TestMainPage(BaseCase):

    @allure.story("Check non filled field")
    @pytest.mark.UI
    def test_TMP001_check_non_filled_field(self):
        main_page_task = MainPage(self.web_driver)
        with allure.step(
            "Check authorization if login and password didn't filled"
        ):
            main_page_task.check_non_filled_field()