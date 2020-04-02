import os,sys

from flask import *
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'     #windows平台
else:
    prefix = 'sqlite:////'    #Mac，Linux平台
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     username = db.Column(db.String(15))

# class Movies(db.Model):
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.Text)
#     year = db.Column(db.String(15))


@app.route('/')
@app.route('/index/')
def index():
    name = '铁柱妹妹'
    movies = [
        {'title':'速度与激情8','year':'2018'},
        {'title':'囧妈','year':'2020'},
        {'title':'烈火英雄','year':'2019'}
    ]

    return render_template('index.html',name=name,movies=movies)

# @app.route('/<name>',endpoint='index')
# def index(name):
#     print(url_for('index',name='hahaha'))
#     return 'helloword:{}'.format(name)
    