from urllib.parse import urljoin
import requests
import os

from requests.sessions import cookiejar_from_dict

from exceptions.exceptions import (
    InvalidLoginException, 
    ResponseErrorException, 
    ResponseStatusCodeException
)
from logger.logger import Logger 
from source.base_page.data import Credentials


class APIBaseClient:
    
    session: requests.Session = requests.Session()


    def __init__(self, url, user, password):
        self.base_url = url
        self.user = user
        self.password = password
        self.csrftoken = None
    
    @property
    def post_headers(self):
        return {
            'Referer': "https://target.my.com/",
        }

    def _request(
        self, 
        method, 
        url, 
        headers=None, 
        data=None, 
        params = None,
        json = None,
        files = None,
        expected_status=200, 
        jsonify=True, 
        allow_redirects = True,
    ):
        logger = Logger()
        logger.log_before_request(url, headers, data, expected_status)
        response = self.session.request(
            method, 
            url, 
            headers=headers, 
            data=data, 
            params=params, 
            json=json, 
            allow_redirects=allow_redirects, 
            files=files,
        )
        logger.log_after_request(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')

        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response.get('sErrorMsg', 'Unknown')
                raise ResponseErrorException(f'Request "{url}" returned error "{error}"')
            return json_response

        return response

class ApiClient(APIBaseClient):
    
    def get_token(self):
        response  = self._request(
            'GET',
            urljoin(self.base_url, "csrf/"),
            jsonify=False
        )
        cookies = response.headers['set-cookie'].split(";")
        csrftoken = [c for c in cookies if 'csrftoken' in c][0]
        if not cookies:
            raise Exception("csrftoken header don't found")

        token = csrftoken.split('=')[-1]
        
        return token
    
    def post_login(self):
        url = "https://auth-ac.my.com/auth"

        headers = self.post_headers

        data = {
            'email': self.user,
            'password': self.password,
            "continue": "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            "failure": "https://account.my.com/login/"
        }

        resp = self._request('POST', url, headers=headers, data=data, jsonify=False)

        if self.session.cookies.get('z') is None:           
            raise InvalidLoginException("Invalid login")

        self.get_token()

        return resp

    def post_create_campaign(self, data: dict) -> dict:
        url = urljoin(self.base_url, "/api/v2/campaigns.json")

        headers = {
            'X-CSRFToken': self.session.cookies.get("csrftoken"),
            'Content-Type': 'application/json',
        }

        return self._request("POST", url, headers=headers, json=data)

    def post_delete_campaign(self, id: int):
        url = urljoin(self.base_url, f"api/v2/campaigns/{id}.json")

        headers = {
            'X-CSRFToken': self.session.cookies.get("csrftoken"),
            'Content-Type': 'application/json',
        }

        data = {
            "status": "deleted"
        }

        return self._request(
            "POST",
            url,
            headers=headers,
            json=data,
            jsonify=False,
            expected_status=204
        )

    def post_send_image(self, file_path: str):
        url_static = urljoin(self.base_url, 'api/v2/content/static.json')
        headers = {
            'X-CSRFToken': self.session.cookies.get('csrftoken')
        }

        files_static = {
            'width': (None, 0),
            'height': (None, 0),
            'file': ('test.jpeg', open(file_path, 'rb'), 'image/jpeg')
        }

        response_static = self._request(
            "POST",
            url_static,
            headers=headers,
            files=files_static,
            jsonify=False
        )
        static = response_static.json()['id']

        return {
            'id_static': static
        }

    def get_url_id(self):
        url = urljoin(self.base_url, f'api/v1/urls/?url={Credentials.CAMPAIGN_LINK}')
        try:
            return self._request("GET", url)['id']
        except:
            raise ResponseErrorException(f"For url='{url}'")

    def get_images_ids(self, repo_root) -> dict:
        image_path = os.path.join(repo_root, 'test.jpeg')
        images_id = self.post_send_image(image_path)

        return {
            'images': {
                'id_static': images_id['id_static']
            }
        }

    def get_campaign(self, campaign_id: int) -> dict:
        return self._request(
            "GET",
            urljoin(
                self.base_url, f"api/v2/campaigns/{campaign_id}.json?fields=id,name,status")
        )