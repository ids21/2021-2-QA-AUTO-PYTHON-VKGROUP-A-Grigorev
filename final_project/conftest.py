import os
import shutil
import pytest
import sys
import logging
import allure
from mysql.builder import MySQLBuilder
from mysql.client import MySQLClient
from api_source.client import ApiClient
from ui_source.fixtures import ui_report, get_driver, web_driver, cookies
from utils.builder import Builder



def pytest_addoption(parser):
    parser.addoption('--url', default='http://myapp_proxy:8070')
    parser.addoption('--vnc', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    if request.config.getoption('--vnc'):
        vnc = True
    else:
        vnc = False

    return {'url': url, 'vnc': vnc}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))

def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/home/aleksandr/test/tests'

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

@pytest.fixture(scope='function')
def fake_data():
    """ Генерация данных для тестов. """
    
    user = Builder.create_user()
    username, password, email = user.username, user.password, user.email

    return {
        'username': username,
        'email': email,
        'password': password
    }

@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MySQLClient()
    yield mysql_client
    mysql_client.connection.close()


@pytest.fixture(scope='session')
def mysql_builder(mysql_client) -> MySQLBuilder:
    return MySQLBuilder(mysql_client)

@pytest.fixture(scope='function')
def api_client(config) -> ApiClient:
    return ApiClient(url = 'http://0.0.0.0:9999/')
    # return ApiClient(config['url'])

@pytest.fixture(scope='function')
def login_api(fake_data, api_client, mysql_builder):
    mysql_builder.add_user(username=fake_data['username'],
                           password=fake_data['password'],
                           email=fake_data['email'])
    api_client.post_login(username=fake_data['username'],
                          password=fake_data['password'])


    return api_client


@pytest.fixture(scope='function', autouse=True)
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')

    log_level = logging.INFO

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
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)