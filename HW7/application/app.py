import json
import os

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


if __name__ == '__main__':
    host = os.environ.get('APP_HOST', '127.0.0.1')
    port = os.environ.get('APP_PORT', '8080')

    app.run(host, port)
