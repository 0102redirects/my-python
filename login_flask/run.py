#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask
from flask import request
from flask.ext.login import fresh_login_required, login_user, logout_user, current_user, LoginManager
from user import get_user, get_anonymous

app = Flask(__name__)
app.secret_key = 'GuCSUePw62Mxl74n'  # 设置secret_key,否则: session is unavailable because no secret key was set

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = get_anonymous


@login_manager.user_loader     # 设置user_loader回调,否则: no user_loader has been installed for this loginmanager
def _user_loader(userid):
    return get_user(userid)    # 向flask-login 提交自定义User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.get_id():
        return ' repeat login!'
    uin = request.json.get('uin', -1)
    try:
        login_user(get_user(uin), remember=True)
    except Exception:
        return 'login failed! maybe uin error...'
    return 'login succeed!'


@app.route('/query', methods=['GET', 'POST'])   # 登录才能查询
@fresh_login_required
def query():
    if current_user.get_id():
        uin = int(current_user.get_id())
        return 'is authenticated'
    return 'anonymous ,not authenticated. please login!'


@app.route('/query_anonymous', methods=['GET', 'POST'])   # 不登录也能查询
def query_anonymous():
    if current_user.is_anonymous():
        return 'anonymous query succeed!'
    return 'query error...'


@app.route('/edit', methods=['POST'])   # 登录才能编辑
@fresh_login_required
def edit():
    return 'edit succeed!'


@app.route('/logout', methods=['GET', 'POST'])
@fresh_login_required
def logout():
    logout_user()
    return 'logout succeed!'


if __name__ == '__main__':
    app.run()
