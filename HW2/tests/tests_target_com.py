from source.main.main_page import MainPage
from source.dashboard.dashboard_page import DashboardPage, ProfilePage
from base import BaseCase

import allure
import pytest

@allure.epic("Dasboard Page")
class TestDashboard(BaseCase):

    @allure.feature("Authorization")
    @pytest.mark.UI
    def test_TDB001_check_non_filled_field(self):
        main_page_task = MainPage(self.web_driver)
        with allure.step(
            "Check authorization if login and password didn't filled"
        ):
            main_page_task.check_non_filled_field()
    

