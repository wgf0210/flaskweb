from text1 import db,app
from text1.models import *
import click


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