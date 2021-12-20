from flask import Flask, jsonify


users = {'Sasha1':1}

mock = Flask(__name__)


class VKMock:

    @staticmethod
    @mock.route('/vk_id/<username>', methods=['GET'])
    def get_vk_id(username):
        if username in users.keys():
            return jsonify({'vk_id': users[username]}), 200
        else:
            return jsonify({'username is not exist'}), 404

    @mock.route('/add_user/<username>', methods=['POST'])
    def add_user(username):
        vk_id = len(users) + 1
        users[username] = vk_id
        return f'User {username} added. VK ID: {vk_id}.', 201

if __name__ == '__main__':
    mock.run(host='0.0.0.0', port=9000)