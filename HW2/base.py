from _pytest.compat import NOTSET
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from source.main.main_page import MainPage
from source.dashboard.dashboard_page import DashboardPage
from conftest import get_driver
from _pytest.fixtures import FixtureRequest
from time import sleep


class BaseCase:

    authorize = False

    @pytest.fixture(scope='session')
    def cookies(self, config):
        web_driver = get_driver(config)
        web_driver.get(config['url'])
        login_page = MainPage(web_driver)
        login_page.login()

        cookies = web_driver.get_cookies()
        web_driver.quit()
        return cookies

    @pytest.fixture(scope='function', autouse=True)
    def set_initial_up(self, web_driver, config, logger, request: FixtureRequest):
        self.web_driver: WebDriver = web_driver
        self.config = config
        self.logger = logger

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            sleep(1)
            for cookie in cookies:
                if 'sameSite' in cookie:
                    if cookie['sameSite'] == 'None':
                        cookie['sameSite'] = 'Strict'
                self.web_driver.add_cookie(cookie)

            self.web_driver.refresh()
            self.dashboard = DashboardPage(self.web_driver)