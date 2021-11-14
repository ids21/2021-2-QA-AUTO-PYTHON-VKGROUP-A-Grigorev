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
        with allure.step(
            "Check authorization if login and password didn't filled"
        ):
            self.main_page.check_non_filled_field()

    @allure.story("Check incorrect credentials")
    @pytest.mark.parametrize('credential', list(['login', 'password']))
    @pytest.mark.UI
    def test_TMP002_check_incorrect_credentials(self, credential):
        with allure.step(
            f"Check authorization if {credential} are incorrect"
        ):
            self.main_page.check_incorrect_credentials(credential)


@allure.epic("Campaign Page")
class TestCampaignPage(BaseCase):

    authorize = True

    @allure.story("Checking creating new campaign")
    @pytest.mark.UI
    def test_TCP001_check_creating_new_campaign(self, repo_root):
        with allure.step("Get campaign page"):
            self.campaign = self.dashboard.get_campaign_page()
        with allure.step("Create campaign"):
            self.campaign.delete_campaign()
            self.campaign.create_campaign(repo_root)
        with allure.step("Did campaign created?"):
            self.campaign.check_campaign_added()
        with allure.step("Post processing"):
            self.campaign.delete_campaign()

@allure.epic("Audiences Page")
class TestAudiencesPage(BaseCase):

    authorize = True

    @allure.story("Checking creating new segments")
    @pytest.mark.UI
    def test_TAP001_check_creating_new_segments(self):
        with allure.step("Get audience page"):
            self.audience = self.dashboard.get_audience_page()
        with allure.step("Create segments"):
            self.audience.create_segments()
        with allure.step("Did segments created?"):
            self.audience.check_segments_added()
        with allure.step("Post processing"):
            self.audience.delete_segments()

    @allure.story("Checking deleting new segments")
    @pytest.mark.UI
    def test_TAP002_check_deleting_new_segments(self):
        with allure.step("Get audience page"):
            self.audience = self.dashboard.get_audience_page()
        with allure.step("Create segments"):
            self.audience.create_segments()
            self.audience.delete_segments()
        with allure.step("Did segments deleted?"):
            self.audience.check_segments_deleted()