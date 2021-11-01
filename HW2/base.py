import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from _pytest.fixtures import FixtureRequest
from time import sleep
import os
import allure

from source.dashboard.dashboard_page import DashboardPage
from source.fixtures import *

class BaseCase:

    authorize = False

    
    @pytest.fixture(scope='function', autouse=True)
    def ui_report(web_driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            screenshoot = os.path.join(temp_dir, 'failure.png')
            web_driver.get_screenshot_as_file(screenshoot)
            allure.attach.file(screenshoot, 'failure.png',
                attachment_type=allure.attachment_type.PNG
            )

            browser_log = os.path.join(temp_dir, 'browser.log')
            with open(browser_log, 'w') as f:
                for i in web_driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            with open(browser_log, 'r') as f:
                allure.attach(f.read(), 'browser.log',
                            attachment_type=allure.attachment_type.TEXT)

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

    