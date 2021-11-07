import pytest
import allure


from api_source.base_api import ApiBase

class SegmentsBase(ApiBase):

    def check_create_segment(self, data):
        get_segment = self.api_client.get_segment(data['id_after_add'])
        try:
            assert get_segment['id'] == data['id_after_add']
            assert get_segment['name'] == data['name']
        except:
            assert False, "Failed to verify segment creation"
        finally:
            self.api_client.post_delete_segment(data['id_after_add'])
            
    @pytest.fixture(scope="function")
    def segment(self) -> dict:
        segment = self.builder.create_segment_data()

        segment_json = self.api_client.post_create_segment(segment)
        segment['id_after_add'] = segment_json['id']

        return segment

@allure.epic("API")
@allure.feature("Audiences")
class TestSegments(SegmentsBase):

    @allure.story("Check create segment")
    @pytest.mark.API
    def test_API_check_create_segment(self, segment):
        self.check_create_segment(segment)