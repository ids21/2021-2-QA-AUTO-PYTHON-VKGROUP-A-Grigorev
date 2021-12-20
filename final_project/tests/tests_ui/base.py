import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver
from ui_source.pages.reg_page import RegistrationPage

from ui_source.pages.main_page import MainPage
from ui_source.pages.login_page import LoginPage
from ui_source.fixtures import *


class BaseCase:

    registration = True

    @pytest.fixture(scope='function', autouse=True)
    def set_initial_up(self, web_driver, config, request: FixtureRequest):
        self.web_driver: WebDriver = web_driver
        self.config = config
        self.login_page = LoginPage(self.web_driver)
        self.registration_page = RegistrationPage(self.web_driver)
        self.main_page = MainPage(self.web_driver)
        if self.registration:
            # cookies = request.getfixturevalue('cookies')
            # for cookie in cookies:
            #     if 'sameSite' in cookie:
            #         if cookie['sameSite'] == 'None':
            #             cookie['sameSite'] = 'Strict'
            #     self.web_driver.add_cookie(cookie)

            # self.web_driver.refresh()
            self.login_page.go_to_registration_page()
            self.registration_page.register()