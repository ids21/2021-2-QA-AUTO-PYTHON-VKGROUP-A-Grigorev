from api_source.exceptions import (
    ResponseErrorException,
    ResponseStatusCodeException
)
from urllib.parse import urljoin
import requests
import allure
import logging

logger = logging.getLogger('test')


class APIBaseClient:

    session: requests.Session = requests.Session()

    def __init__(self, url):
        self.base_url = url
        self.session: requests.Session = requests.Session()

    @staticmethod
    def log_pre(method, url, headers, data):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
        )

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  f'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > 500:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {500}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    def _request(
        self,
        method,
        location,
        data=None,
        headers=None,
        json=None,
        expected_status=200,
    ):
        url = urljoin(self.base_url, location)
        self.log_pre(method, url, headers, data)
        response = self.session.request(
            method,
            url,
            headers=headers,
            data=data,
            json=json
        )

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(
                f'Got {response.status_code} {response.request} for URL "{url}"')

        self.log_post(response)

        return response


class ApiClient(APIBaseClient):

    @allure.step('Авторизация пользователя')
    def post_login(self, username, password, expected_status=200):
        location = '/login'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        if username and password:
            data = {
                'username': username,
                'password': password,
                'submit': 'Login'
            }
        elif password is None:
            data = {
                'username': username,
                'submit': 'Login'
            }

        response = self._request(
            'POST', location, headers=headers, data=data, expected_status=expected_status)

        return response

    @allure.step('Добавление пользователя через API')
    def post_add_user(self, username, password, email, expected_status=201):
        location = '/api/add_user'

        headers = {
            'Content-Type': 'application/json'
        }

        if username and password and email:
            data = {
                "username": username,
                "password": password,
                "email": email
            }
        elif email is None:
            data = {
                "username": username,
                "password": password
            }

        response = self._request(
            'POST', location, headers=headers, json=data, expected_status=expected_status)

        return response

    @allure.step('Удаление пользователя')
    def get_delete_user(self, username, expected_status=204):
        location = f'/api/del_user/{username}'

        response = self._request(
            'GET', location, expected_status=expected_status)

        return response

    @allure.step('Блокировка пользователя')
    def get_block_user(self, username, expected_status=200):
        location = f'/api/block_user/{username}'

        response = self._request(
            'GET', location, expected_status=expected_status)

        return response

    @allure.step('Разблокировка пользователя')
    def get_unblock_user(self, username, expected_status=200):
        location = f'/api/accept_user/{username}'

        response = self._request(
            'GET', location, expected_status=expected_status)

        return response
