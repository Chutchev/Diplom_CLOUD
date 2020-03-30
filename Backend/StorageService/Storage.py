from flask import Flask, request, jsonify, make_response,send_file, send_from_directory
from flask_cors import CORS
# from flask_uploads import *
import json
from DBExecutor import *
import requests
from helpers import *
import os
app = Flask(__name__)
CORS(app)
app.debug = True


@app.route('/files', methods=['post', 'get'])
def get_files():
    if request.method == 'POST':
        token = json.loads(request.data)['token']
        response = requests.post('http://127.0.0.1:5000/auth', data=token)
        info = response.json()['data']
        print(info)
        files_in_dir = get_file('IVANCHUTCHEV')
        return jsonify(list(files_in_dir))

@app.route('/files/<filename>', methods=['get'])
def download(filename):
    filepath = get_filepath(filename)[0]
    print(filepath)
    return send_file(filepath, as_attachment=True)
    # return send_from_directory(filepath, filename=filename)


# @app.route('/upload', methods=['post', 'get'])
# def upload():
#     media = UploadSet('media', default_dest=lambda app: app.instance_root)
#
if __name__ == '__main__':
    app.run(port=6556)