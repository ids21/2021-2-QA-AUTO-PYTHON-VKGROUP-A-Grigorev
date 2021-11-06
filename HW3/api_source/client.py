from urllib.parse import urljoin
import requests
from requests.cookies import cookiejar_from_dict

from exceptions.exceptions import (
    InvalidLoginException, 
    ResponseErrorException, 
    ResponseStatusCodeException
)
from logger.logger import Logger 


class ApiClient:

    def __init__(self, url, user, password):
        self.base_url = url
        self.user = user
        self.password = password

        self.session = requests.Session()
        self.csrf_token = None
        self.session_id_gtp = None
    
    @property
    def post_headers(self):
        return {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1",
        }

    def _request(
        self, 
        method, 
        url, 
        headers=None, 
        data=None, 
        expected_status=200, 
        jsonify=True, 
        allow_redirects = True
    ):
        logger = Logger()
        logger.log_before_request(url, headers, data, expected_status)
        response = self.session.request(method, url, headers=headers, data=data, allow_redirects=allow_redirects)
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
    
    def post_login(self):
        url = "https://account.my.com/login/"

        headers = self.post_headers

        data = {
            'email': self.user,
            'password': self.password,
            "continue": "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
        }

        resp = self._request('POST', url, headers=headers, data=data, jsonify=False)
        
        try:
            response_cookies = resp.headers['Set-Cookie'].split(';')
            self.csrf_token = [c for c in response_cookies if 'csrf_token' in c][0].split('=')[-1]
            self.session.cookies = cookiejar_from_dict({
                'csrf_token': self.csrf_token,
                })
        except Exception as e:
            raise InvalidLoginException(e)

        return resp

    def get_token(self):
        response  = self._request(
            'GET',
            urljoin(self.base_url, "csrf/"),
            jsonify=False
        )
        cookies = response.headers['set-cookie'].split(";")
        csrf_token = [c for c in cookies if 'csrftoken' in c]
        if not cookies:
            raise Exception('No csrftoken header found in main page headers')

        token = csrf_token.split('=')[-1]
        return token