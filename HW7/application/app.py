import json
import os
import threading
import settings

from flask import Flask, request, jsonify

app = Flask(__name__)


USER_DATA = {
    'Sasha': 22,
    'Aybulat': 21,
    'Andrey': 21,
}


@app.route('/create_user', methods=['POST'])
def create_user():
    name = json.loads(request.data)["name"]
    age = json.loads(request.data)["age"]
    if USER_DATA.get(name) is None:
        USER_DATA[name] = age
        data = {'name': name, 'age': age}
        return jsonify(data), 201
    else:
        return jsonify(f'{name} already exists'), 400 


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST,
        'port': settings.APP_PORT
    })
    server.start()
    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    terminate_func()


@app.get('/shutdown')
def shutdown():
    shutdown_app()
    return jsonify('Bye (^.^)/'), 200
