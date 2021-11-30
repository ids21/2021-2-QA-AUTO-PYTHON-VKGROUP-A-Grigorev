import time
import requests
from requests.exceptions import ConnectionError


class Waiter:
    
    @staticmethod
    def wait_ready(host, port):
        started = False
        st = time.time()
        while time.time() - st <= 10:
            try:
                requests.get(f'http://{host}:{port}')
                started = True
                break
            except ConnectionError:
                pass

        if not started:
            raise RuntimeError(f'{host}:{port} did not started in 10s!')