from flask import Flask
import json


users = {'Sasha1':1}

mock = Flask(__name__)


@mock.route('/vk_id/<username>', methods=['GET'])
def get_vk_id(username):
    if username in users.keys():
        return json.dumps({'vk_id': users[username]}), 200
    else:
        return json.dumps({}), 404


if __name__ == '__main__':
    mock.run(host='0.0.0.0', port=9000)