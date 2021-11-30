from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import logging

from source.main.main_page import MainPage


def get_driver(config, download_dir=None):
    browser_name = config['browser_name']
    selenoid = config['selenoid']
    vnc = config['vnc']
    version = config['version']
    options = Options()
    if selenoid:
        options.add_experimental_option(
            "prefs", {"download.default_directory": '/home/selenium/Downloads'}
        )
        capabilities = {
            'browserName': 'chrome',
            'version': '80.0'
        }
        if vnc:
            capabilities['enableVNC'] = True

        browser = webdriver.Remote(
            selenoid,
            options=options,
            desired_capabilities=capabilities
        )
    else:
        if browser_name == 'chrome':
            if download_dir is not None:
                options.add_experimental_option(
                    "prefs", {"download.default_directory": download_dir}
                )
            manager = ChromeDriverManager(
                version='latest',
                log_level=logging.CRITICAL
            )
            browser = webdriver.Chrome(
                executable_path=manager.install(),
                options=options
            )
        elif browser_name == 'firefox':
            if download_dir is not None:
                options.add_experimental_option(
                    "prefs", {"browser.download.dir": download_dir}
                )

            manager = GeckoDriverManager(version='latest')
            browser = webdriver.Firefox(
                executable_path=manager.install(),
                options=options
            )
        else:
            raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    browser.implicitly_wait(0.2)
    return browser


@pytest.fixture(scope='function')
def web_driver(config) -> object:
    url = config['url']
    web_driver = get_driver(config)
    web_driver.get(url)

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='session')
def cookies(config):
    web_driver = get_driver(config)
    web_driver.get(config['url'])
    login_page = MainPage(web_driver)
    login_page.login()

    cookies = web_driver.get_cookies()
    web_driver.quit()
    return cookies