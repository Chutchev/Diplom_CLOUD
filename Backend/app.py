from flask import Flask, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['post'])
def hello_world():
    if request.method == 'POST':
        print(json.loads(request.data))
    return 'dfjkg'


if __name__ == '__main__':
    app.run()
