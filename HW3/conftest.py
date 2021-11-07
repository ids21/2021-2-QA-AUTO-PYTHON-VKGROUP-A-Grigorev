import os
import sys
import shutil
from pytest import fixture
import logging
import allure

from source.fixtures import *
from api_source.client import ApiClient
from source.base_page.data import Credentials

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


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(
        request.config.base_temp_dir,
        request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    )
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))



@pytest.fixture(scope='session')
def api_client(config):
    credentials = dict(
        user=Credentials.USERNAME,
        password=Credentials.PASSWORD
    )
    return ApiClient(config['url'], **credentials)
