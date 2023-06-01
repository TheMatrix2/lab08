# Сервер

from flask import Flask, request, jsonify
from math import sqrt

app = Flask(__name__)


@app.route('/distance', methods=['GET'])
def distance():
    x1 = float(request.args.get('x1'))
    y1 = float(request.args.get('y1'))
    x2 = float(request.args.get('x2'))
    y2 = float(request.args.get('y2'))
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return jsonify({'distance': d})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
