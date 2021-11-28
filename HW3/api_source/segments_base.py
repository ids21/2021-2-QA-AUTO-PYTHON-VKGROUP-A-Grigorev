import pytest

from api_source.base_api import ApiBase


class SegmentsBase(ApiBase):

    def check_create_segment(self, data):
        get_segment = self.api_client.get_segment(data['id'])
        try:
            assert get_segment['id'] == data['id']
            assert get_segment['name'] == data['name']
        except:
            assert False, "Failed to verify segment creation"
        finally:
            self.api_client.post_delete_segment(data['id'])

    @pytest.fixture(scope="function")
    def create_segment(self) -> dict:
        segment = self.builder.create_segment_data()

        segment_json = self.api_client.post_create_segment(segment)

        return segment_json

    def check_delete_segment(self, data):
        try:
            self.api_client.post_delete_segment(data['id'])
        except:
            assert False, "error occurred during delete segment"