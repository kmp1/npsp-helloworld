import os
from flask import Flask
import numpy
import scipy.stats


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/numpy')
def numpy_tests():
    numpy.linalg.test('fast')
    return 'linalg tests: done'


@app.route('/scipy')
def scipy_tests():
    scipy.stats.test('fast')
    return 'scipy.stats.tests: done'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
