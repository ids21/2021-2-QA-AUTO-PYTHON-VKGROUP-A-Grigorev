import pytest
import allure

from api_source.campaign_base import CampaignsBase

@allure.epic("API")
@allure.feature("Campaign")
class TestCampaign(CampaignsBase):

    @allure.story("Check create campaign")
    @pytest.mark.API
    def test_API_check_create_campaign(self, create_campaign):
        self.check_create_campaign(create_campaign)