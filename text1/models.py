from text1 import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

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