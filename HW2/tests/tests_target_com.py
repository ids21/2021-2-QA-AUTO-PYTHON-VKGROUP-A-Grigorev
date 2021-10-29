from source.main.main_page import MainPage
from source.dashboard.dashboard_page import DashboardPage
from source.dashboard.campaign_page import CampaignPage
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
    
    @allure.story("Check incorrect credentials")
    @pytest.mark.parametrize('credential', list(['login','password']))
    @pytest.mark.UI
    def test_TMP002_check_incorrect_credentials(self, credential):
        main_page_task = MainPage(self.web_driver)
        with allure.step(
            f"Check authorization if {credential} are incorrect"
        ):
            main_page_task.check_incorrect_credentials(credential)

@allure.epic("Campaign Page")
class TestCampaignPage(BaseCase):

    authorize = True

    @allure.story("Checking creating new campaign")
    @pytest.mark.UI
    def test_TCP001_check_creating_new_campaign(self):
        with allure.step("Get campaign page"):
            self.campaign = self.dashboard.get_campaign_page()
        with allure.step("Create campaign"):
            self.campaign.delete_campaign()
            self.campaign.create_campaign()
        with allure.step("Did campaign get created"):
            self.campaign.check_campaign_added()
        with allure.step("Post processing"):
            self.campaign.delete_campaign()

    @allure.story("Checking deleting campaign")
    @pytest.mark.UI
    def test_TCP002_check_delete_campaign(self):
        with allure.step("Get campaign page"):
            self.campaign = self.dashboard.get_campaign_page()
        with allure.step("Pre processing"):
            self.campaign.delete_campaign()
            self.campaign.create_campaign()
            self.campaign.delete_campaign()
        with allure.step("Did campaign get deleted"):
            self.campaign.check_campaign_deleted()
