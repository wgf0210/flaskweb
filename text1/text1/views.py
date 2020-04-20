from text1 import app,db
from flask import Flask,render_template,render_template,request,flash,url_for,redirect
from flask_login import login_user,logout_user,login_required,current_user
from text1.models import *

@app.route('/',methods=['GET','POST'])
# @app.route('/index/')
def index():
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
    return render_template('index.html',movies=movies,len=lens)

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

# @app.route('/<name>',endpoint='index')
# def index(name):
#     print(url_for('index',name='hahaha'))
#     return 'helloword:{}'.format(name)

