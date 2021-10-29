import os
import sys
import shutil
from pytest import fixture
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure



DEFAULT_BROWSER = "chrome"
DEFAULT_VERSION_BROWSER = "94.0"


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
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--debug_log', action='store_true')


@fixture(scope='session')
def config(request):
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption('--url')
    version = request.config.getoption('--browser_version')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        selenoid = 'http://localhost:4444/wd/hub/'
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
    else:
        selenoid = None
        vnc = False

    return {
        'browser_name': browser_name,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'version': version,
    }

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


@fixture(scope='function')
def web_driver(config, temp_dir) -> object:
    url = config['url']
    web_driver = get_driver(config, download_dir=temp_dir)
    web_driver.get(url)

    yield web_driver
    web_driver.quit()


@fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
    )
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(
            f.read(),
            'test.log',
            attachment_type=allure.attachment_type.TEXT
        )

def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(
        request.config.base_temp_dir,
        request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    )
    os.makedirs(test_dir)
    return test_dir

@fixture(scope='function', autouse=True)
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