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
PATH = os.path.abspath('../FILES')


@app.route('/upload', methods=['post'])
def upload_file():
    response = {'SUCCESS': False}
    if request.method == 'POST':
        files = dict(request.files)
        for f in files.values():
            fullpath = os.path.join(PATH, f.filename)
            f.save(dst=fullpath)
            md5_sum = read_hash(fullpath)
            add_file(f.filename, fullpath, 'IVANCHUTCHEV', f.filename.split('.')[-1], md5_sum)
        response = {'SUCCESS': True}
    return jsonify(response)


@app.route('/files', methods=['post', 'get', 'delete'])
def get_files():
    if request.method == 'POST':
        response_from_ui = json.loads(request.data)
        token = response_from_ui['token']
        response = requests.post('http://127.0.0.1:5000/auth', data=token)
        info = response.json()['data']
        if response_from_ui.get('DELETE'):
            filename = response_from_ui.get('filename')
            filepath = get_filepath(filename)[0]
            data = delete_file(filename)
            answer = {'DELETED': True,
                      'filename': filename}
            os.remove(filepath)
            return jsonify(answer)
        else:
            files_in_dir = get_file('IVANCHUTCHEV')
            return jsonify(list(files_in_dir))

@app.route('/files/<filename>', methods=['get'])
def download(filename):
    filepath = get_filepath(filename)[0]
    print(filepath)
    return send_file(filepath, as_attachment=True)
    # return send_from_directory(filepath, filename=filename)

if __name__ == '__main__':
    app.run(port=6556)