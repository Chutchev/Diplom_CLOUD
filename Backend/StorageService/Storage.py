from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
# from flask_uploads import *
import json
from DBExecutor import *
import os
app = Flask(__name__)
CORS(app)
app.debug = True


@app.route('/files', methods=['post', 'get'])
def get_files():
    if request.method == 'POST':
        token = request.data
        print(token)
        files_in_dir = get_file('IVANCHUTCHEV')
        return jsonify(list(files_in_dir))

# @app.route('/upload', methods=['post', 'get'])
# def upload():
#     media = UploadSet('media', default_dest=lambda app: app.instance_root)
#
if __name__ == '__main__':
    app.run(port=6556)