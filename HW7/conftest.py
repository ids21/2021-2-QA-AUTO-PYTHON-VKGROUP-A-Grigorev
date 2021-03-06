import os
import sys
import shutil
import signal
import subprocess
import logging
import pytest
from copy import copy
import requests
import settings

from utils.waiter import Waiter

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


class App:

    def start_app(self, config):
        from application import app
        app.run_app()

        Waiter.wait_ready(settings.APP_HOST, settings.APP_PORT)

    def stop_app(self, config):
        requests.get(
            f'http://{settings.APP_HOST}:{settings.APP_PORT}/shutdown')


class Mock:

    def start_mock(self):
        from mock import flask_mock
        flask_mock.run_mock()

        Waiter.wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)

    def stop_mock(self):
        requests.get(
            f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        App().stop_app(config)
        Mock().stop_mock()


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):  # in master only
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.makedirs(base_dir)

        App().start_app(config)
        Mock().start_mock()

    config.base_temp_dir = base_dir  # everywhere


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir,
                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function', autouse=True)
def logger(temp_dir):
    log_formatter = logging.Formatter(
        '%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')

    log_level = logging.DEBUG

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()