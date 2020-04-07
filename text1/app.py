import os,sys

from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
import click

WIN = sys.platform.startswith('win')   #系统平台是否以win开头
if WIN:
    prefix = 'sqlite:///'     #windows平台
else:
    prefix = 'sqlite:////'    #Mac，Linux平台
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flask_dev'

db = SQLAlchemy(app)
login_manager = LoginManager(app) # 实例化扩展类
@login_manager.user_loader
def load_user(user_id):     # 创建用户加载回调函数，接收用户id为参数
    user = User.query.get(user_id)
    return user
# 若操作前未登录，系统会跳转到登录页面
login_manager.login_view = 'login'

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(15))
    username = db.Column(db.String(15))
    pwd_hash = db.Column(db.String(128))
    def set_password(self,password):
        self.pwd_hash = generate_password_hash(password)  #生成加密密码
    def validate_password(self,password):
        return check_password_hash(self.pwd_hash,password)  #检验加密密码

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
    print(current_user)
    movies = Movies.query.filter().order_by(Movies.year.desc())
    lens = 0
    for i in movies:
        lens += 1
    if request.method == 'POST':
        if not current_user.is_authenticated:      #登陆判断
            return redirect(url_for('login'))
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

@app.route('/movie/editor/<int:movie_id>',methods=['GET','POST'])
@login_required       #登陆判断
def editor(movie_id):
    # get_or_404有则返回，没有返回404错误
    e_movie = Movies.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if title and year and len(year) < 15:
            e_movie.title = title
            e_movie.year = year
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('index'))
        else:
            flash('输入有误')
            return redirect(url_for('editor',movie_id=movie_id))
    return render_template('editor.html',e_movie=e_movie)

@app.route('/movie/dele/<int:movie_id>',methods=["GET","POST"])
@login_required
def dele(movie_id):
    d_movie = Movies.query.get_or_404(movie_id)
    db.session.delete(d_movie)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('index'))

@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            user = User.query.first()
            if username == user.username and user.validate_password(password):
                login_user(user)
                flash('登陆成功')
                return redirect(url_for('index'))
            else:
                flash('登录失败')
            return redirect(url_for('login'))
        else:
            flash('输入错误')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('退出成功')
    return redirect(url_for('index'))

@app.route('/settings/',methods=["GET","POST"])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']
        if name and len(name)<20:
            current_user.name = name
            db.session.commit()
            flash('设置完成')
            return redirect(url_for('index'))
        else:
            flash('输入错误')
            return redirect(url_for('settings'))
    return render_template('settings.html')

# 处理错误页面/信息函数
@app.errorhandler(404)
def error_page(e):        # e--给定一个参数来接受
    return render_template('404.html')

# 自定义命令-----创建数据库
@app.cli.command()    #把下面的代码注册为命令
@click.option('--drop',is_flag=True,help='先删除在创建')  #is_flag为True就有了判断条件
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')
    
# 自定义命令-----向空数据库中插入数据    
@app.cli.command()
def forge():
    # name = '铁柱妹妹'
    movies = [
        {'title':'叶问3','year':'2012'},
        {'title':'疯狂外星人','year':'2019'},
        {'title':'大赢家','year':'2020'}
    ]
    # user = User(username=name)
    # db.session.add(user)
    for i in movies:
        movie = Movies(title=i['title'],year=i['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('数据库插入数据完成')

# 自定义指令-----生成管理员账号,输入用户名admin，密码，确认密码
@app.cli.command()
@click.option('--username',prompt=True,help='登录的用户名')  #option--必写
@click.option('--password',prompt=True,help='登录的密码',confirmation_prompt=True,hide_input=True)# 二次密码，密码非明文
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员用户')
        user.username = username
        user.set_password = password
    else:
        click.echo('创建管理员用户')
        user = User(username=username,name='admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('管理员账号更新/创建完成')




# @app.route('/<name>',endpoint='index')
# def index(name):
#     print(url_for('index',name='hahaha'))
#     return 'helloword:{}'.format(name)