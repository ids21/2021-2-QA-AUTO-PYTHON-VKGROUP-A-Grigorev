import json
import logging
import socket

logger = logging.getLogger('test')


class SocketClient:

    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1)
        self.client.connect((self.host, self.port))

    @staticmethod
    def log_pre(request):
        logger.info(f'\nREQUEST:\n{request}')

    @staticmethod
    def log_post(response):
        status_code = response[0].split(' ')[1]
        logger.info(
            f'\nRESPONSE:\n'
            f'{status_code}\n'
            f'{response[1:-2]}\n'
            f'{response[-1]}\n'
        )

    def post(self, params, data):
        json_data = json.dumps(data, indent=4)

        request = f'POST {params} HTTP/1.1\r\n' \
                  f'Host: {self.host}\r\n' \
                  f'PORT: {self.port}\r\n' \
                  f'Content-Length: {len(json_data)}\r\n' \
                  f'Content-Type: application/json\r\n\r\n' \
                  f'{json_data}\r\n\r\n'
        self.log_pre(request)

        self.client.send(request.encode())
        response = self.get_response_data(self.client)

        return response

    def get(self, params):
        request = f'GET {params} HTTP/1.1\r\n' \
                  f'Host:{self.host}:{self.port}\r\n\r\n'
        self.log_pre(request)

        self.client.send(request.encode())
        response = self.get_response_data(self.client)

        return response

    def put(self, params, data):
        json_data = json.dumps(data, indent=4)

        request = f'PUT {params} HTTP/1.1\r\n' \
                  f'Host: {self.host}\r\n' \
                  f'Content-Length: {len(json_data)}\r\n' \
                  f'Content-Type: application/json\r\n\r\n' \
                  f'{json_data}\r\n\r\n'
        self.log_pre(request)

        self.client.send(request.encode())
        response = self.get_response_data(self.client)

        return response

    def delete(self, params):
        request = f'DELETE {params} HTTP/1.1\r\n'\
                  f'Host: {self.host}\r\n'\
                  f'Port: {self.port}\r\n\r\n'\

        self.log_pre(request)

        self.client.send(request.encode())
        response = self.get_response_data(self.client)

        return response

    def get_response_data(self, client):
        total_data = []

        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                client.close()
                break

        data = ''.join(total_data).splitlines()
        
        self.log_post(data)

        return {'status_code': int(data[0].split(' ')[1]), 'body': data[-1]}
