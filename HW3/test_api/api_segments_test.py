import pytest
import allure


from api_source.segments_base import SegmentsBase


@allure.epic("API")
@allure.feature("Audiences")
class TestSegments(SegmentsBase):

    @allure.story("Check create segment")
    @pytest.mark.API
    def test_API_check_create_segment(self, create_segment):
        self.check_create_segment(create_segment)

    @allure.story("Check delete segment")
    @pytest.mark.API
    def test_API_check_delete_segment(self, create_segment):
        segment_data = create_segment
        self.check_delete_segment(segment_data)