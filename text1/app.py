import os,sys

from flask import *
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'     #windows平台
else:
    prefix = 'sqlite:////'    #Mac，Linux平台
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flask_dev'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(15))

class Movies(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.Text)
    year = db.Column(db.String(15))

# 模板上下文处理函数
@app.context_processor
def app_all():
    name = User.query.first().username
    return dict(name=name)

@app.route('/',methods=['GET','POST'])
# @app.route('/index/')
def index():
    movies = Movies.query.filter().order_by(Movies.year.desc())
    lens = 0
    for i in movies:
        lens += 1
    if request.method == 'POST':
        # 获取表单数据
        title = request.form.get('title')
        year = request.form.get('year')
        print(year)
        # 验证数据
        if title and year and len(year)<15:
            db.session.add(Movies(title=title,year=year))
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('index'))
        else:
            flash('格式错误')
            return redirect(url_for('index'))
    return render_template('index.html',movies=movies,lens=len)

# 处理错误页面/信息函数
@app.errorhandler(404)
def error_page(e):        # e--给定一个参数来接受
    return render_template('404.html')

# @app.route('/<name>',endpoint='index')
# def index(name):
#     print(url_for('index',name='hahaha'))
#     return 'helloword:{}'.format(name)

# 自定义命令创建数据库
@app.cli.command()    #把下面的代码注册为命令
@click.option('--drop',is_flag=True,help='先删除在创建')  #is_flag为True就有了判断条件
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')
# 自定义命令向空数据库中插入数据    
@app.cli.command()
def forge():
    name = '铁柱妹妹'
    movies = [
        {'title':'叶问3','year':'2012'},
        {'title':'疯狂外星人','year':'2019'},
        {'title':'大赢家','year':'2020'}
    ]
    user = User(username=name)
    db.session.add(user)
    for i in movies:
        movie = Movies(title=i['title'],year=i['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('数据库插入数据完成')
