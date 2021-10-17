from pytest import fixture, UsageError
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

DEFAULT_BROWSER = "chrome"
DEFAULT_VERSION_BROWSER = "94.0"
CHROME = "chrome"
FIREFOX = "firefox"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default=DEFAULT_BROWSER,
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        '--browser_version',
        action='store',
        default=DEFAULT_VERSION_BROWSER,
        help="Choose version"
    )
    parser.addoption('--url', default='https://target.my.com/')


@fixture(scope='function')
def web_driver(request) -> object:
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption('--url')
    options_chrome = ChromeOptions()
    options_firefox = FirefoxOptions()
    if browser_name == CHROME:
        options_chrome.add_argument("--browser_version")
        web_driver = webdriver.Chrome(
            executable_path="drivers/chromedriver",
            options=options_chrome
        )
    elif browser_name == FIREFOX:
        options_firefox.add_argument("--browser_version")
        web_driver = webdriver.Firefox(
            executable_path="drivers/geckodriver",
            options=options_firefox
        )
    else:
        raise UsageError("--browser_name should be chrome or firefox")    
    web_driver.implicitly_wait(1)
    web_driver.maximize_window()
    web_driver.get(url)
    yield web_driver
    web_driver.close()
