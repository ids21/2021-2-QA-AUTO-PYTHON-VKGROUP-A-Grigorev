import json
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

from application.app import USER_DATA


@app.route('/get_age/<name>', methods=['GET'])
def get_user_age(name):
    if age := USER_DATA.get(name):
        data = {'name': name, 'age': age}
        return jsonify(data), 200
    else:
        return jsonify(f'{name} does not exist'), 404


@app.route('/edit_age', methods=['PUT'])
def edit_user():
    name = json.loads(request.data)['name']
    if USER_DATA.get(name) is not None:
        new_age = json.loads(request.data)['new_age']
        USER_DATA[name] = new_age
        data = {'name': name, 'age': new_age}
        return jsonify(data), 201
    else:
        return jsonify(f'{name} does not exist'), 404


@app.route("/delete_record/<name>", methods=["DELETE"])
def delete_user(name):
    if name in USER_DATA:
        USER_DATA.pop(name)
        return jsonify({"status": "Ok"}), 200
    else:
        return jsonify(f'User {name} not found and not deleted'), 404



def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Bye (^.^)/'), 200