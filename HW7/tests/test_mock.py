import json
from mock.flask_mock import USER_DATA
from client.socket_client import SocketClient
from settings import APP_PORT, APP_HOST, MOCK_HOST, MOCK_PORT


class TestPostRequests:

    def test_create_user(self):
        client = SocketClient(host=APP_HOST, port=APP_PORT)
        test_user = dict(name="Tom", age=1)
        resp = client.post('/create_user', test_user)
        assert resp['status_code'] == 201

        body = json.loads(resp['body'])
        assert body['name'] == test_user['name']
        assert body['age'] == test_user['age']


class TestGetRequests:

    def test_get_age(self):
        client = SocketClient(host=MOCK_HOST, port=MOCK_PORT)
        name = "Andrey"
        resp = client.get(f'/get_age/{name}')
        assert resp['status_code'] == 200

        body = json.loads(resp['body'])
        assert body['age'] == USER_DATA[name]


class TestDeleteRequests:

    def test_delete_user(self):
        client = SocketClient(host=MOCK_HOST, port=MOCK_PORT)
        name='Aybulat'
        resp = client.delete(f"/delete_record/{name}")
        assert resp['status_code'] == 200

    def test_delete_non_existed_user(self):
        client = SocketClient(host=MOCK_HOST, port=MOCK_PORT)
        name = 'Federico'
        resp = client.delete(f'/delete_record/{name}')
        assert resp['status_code'] == 404


class TestPutRequests:

    def test_change_age(self):
        client = SocketClient(host=MOCK_HOST, port=MOCK_PORT)
        user = dict(name='Andrey', new_age=23)
        resp = client.put('/edit_age', user)
        assert resp['status_code'] == 201

        body = json.loads(resp['body'])
        assert body['age'] == user['new_age']
