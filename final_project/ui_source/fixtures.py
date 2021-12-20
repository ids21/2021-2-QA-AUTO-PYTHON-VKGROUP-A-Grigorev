import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.builder import Builder
from ui_source.pages.login_page import LoginPage



@pytest.fixture(scope='function')
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


def get_driver(config, download_dir=None):
    vnc = config['vnc']
    options = Options()
    selenoid = 'http://127.0.0.1:4444/wd/hub/'
    options.add_experimental_option(
        "prefs", {"download.default_directory": '/home/selenium/Downloads'}
    )
    capabilities = {
        'browserName': 'chrome',
        'version': '88.0'
    }
    capabilities['enableVNC'] = True
    browser = webdriver.Remote(
        selenoid,
        options=options,
        desired_capabilities=capabilities
    )
    browser.maximize_window()
    browser.implicitly_wait(1)
    return browser


@pytest.fixture(scope='function')
def web_driver(config) -> object:
    url = config['url']
    web_driver = get_driver(config)
    web_driver.get(url)

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='session')
def cookies(config, mysql_builder):
    web_driver = get_driver(config)
    web_driver.get(config['url'])
    login_page = LoginPage(web_driver)
    user = Builder.create_user()
    username, password, email = user.username, user.password, user.email
    mysql_builder.add_user(username, password, email)
    login_page.login(username, password)
    cookies = web_driver.get_cookies()
    web_driver.quit()
    return cookies
