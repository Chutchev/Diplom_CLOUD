from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import helpers
import os
app = Flask(__name__)
CORS(app)
app.debug = True

@app.route('/myfiles', methods=['post', 'get'])
def myfiles():
    if request.method == 'POST':
        path = os.path.abspath('app.py')
    else:
        path = 'FILE NOT FOUND'
    return jsonify(path)


@app.route('/login', methods=['post'])
def login():
    result = {'is_autorised': False, 'token': None}
    if request.method == 'POST':
        credentials = json.loads(request.data)
        login, password = credentials['login'], credentials['password']
        if login and password:
            result['is_autorised'] = True
            token = str(helpers.generate_token(login, data='IVAN'), encoding='utf-8')
            result['token'] = token
    return jsonify(result)


if __name__ == '__main__':
    app.run()
