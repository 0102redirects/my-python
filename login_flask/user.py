#!/usr/bin/env python
# -*- coding: utf8 -*-


class User(object):
    """
    自定义User, 在登录时提交给 flask-login 模块
    """
    def __init__(self, uin):
        self.uin = uin

    def is_active(self):
        return not self.is_anonymous()

    def is_authenticated(self):
        return not self.is_anonymous()

    def is_anonymous(self):
        return self.uin == 10000

    def get_id(self):
        if not self.is_anonymous():
            return str(self.uin)
        else:
            return None


def get_user(uin):
    uin = int(uin)
    if uin >= 10000:    # uin 从10000开始,匿名用户为10000
        print uin
        return User(uin)
    else:
        return None


def get_anonymous():
    return User(10000)
