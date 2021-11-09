import pytest
import allure


from api_source.base_api import ApiBase

class CampaignsBase(ApiBase):

    def check_create_campaign(self, data):
        get_campaign = self.api_client.get_campaign(data['id_after_add'])
        try:
            assert get_campaign['id'] == data['id_after_add']
            assert get_campaign['name'] == data['name']
        except:
            assert False, "Failed to verify campaign creation"

    @pytest.fixture(scope="function")
    def campaign(self, repo_root):
        id_image = self.api_client.get_images_ids(repo_root)
        id_url = self.api_client.get_url_id()
        data = self.builder.create_campaign_data()
        id_static = id_image['images']['id_static']
        data['banners'][0]['urls']['primary']['id'] = id_url
        data['banners'][0]['content']['image_240x400']['id'] = id_static

        campaign_json = self.api_client.post_create_campaign(data)

        data['id_after_add'] = campaign_json['id']
        yield data

        self.api_client.post_delete_campaign(data['id_after_add'])

@allure.epic("API")
@allure.feature("Campaign")
class TestCampaign(CampaignsBase):

    @allure.story("Check create campaign")
    @pytest.mark.API
    def test_API_check_create_campaign(self, campaign):
        self.check_create_campaign(campaign)