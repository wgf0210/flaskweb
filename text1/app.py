from flask import *

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():

#     return 'helloword'

@app.route('/<name>',endpoint='index')
def index(name):
    print(url_for('index',name='hahaha'))
    return 'helloword:{}'.format(name)