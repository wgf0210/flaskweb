from text1 import app
from flask import render_template

# 处理错误页面/信息函数
@app.errorhandler(404)
def error_page(e):        # e--给定一个参数来接受
    return render_template('404.html')

