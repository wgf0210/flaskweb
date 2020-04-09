import os,sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy    #处理ORM模型
from flask_login import LoginManager


# Flask
app = Flask(__name__)

# ORM模型
WIN = sys.platform.startswith('win')   #系统平台是否以win开头
if WIN:
    prefix = 'sqlite:///'     #windows平台
else:
    prefix = 'sqlite:////'    #Mac，Linux平台

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev')
db = SQLAlchemy(app)

# LoginManager
login_manager = LoginManager(app) # 实例化扩展类
@login_manager.user_loader
def load_user(user_id):     # 创建用户加载回调函数，接收用户id为参数
    from text1.models import User
    user = User.query.get(user_id)
    return user
# 若操作前未登录，系统会跳转到登录页面
login_manager.login_view = 'login'


# 模板上下文处理函数
@app.context_processor
def con_all():
    from text1.models import User
    name = User.query.first().username
    return dict(name=name)

from text1 import views,commands,errors