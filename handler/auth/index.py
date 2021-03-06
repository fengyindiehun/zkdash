#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014,掌阅科技
All rights reserved.

摘    要: index.py
创 建 者: zhuangshixiong
创建日期: 2015-10-09
"""
from handler.bases import CommonBaseHandler
from lib import route


@route(r'/')
class IndexHandler(CommonBaseHandler):

    '''配置管理系统页面入口
    '''

    #def response(self):
    #    return self.render('index.html')

    def response(self):
        #return self.render('index.html')
        return self.render('login.html')

@route(r'/login', '登录验证')
class LoginMainHandler(CommonBaseHandler):

    '''首页
    '''

    def response(self):
        username = self.get_argument('username')
        password = self.get_argument('passwordhash')
        self.set_secure_cookie('username', username)
        self.render('index.html')


@route(r'/auth/index/main', '首页')
class IndexMainHandler(CommonBaseHandler):

    '''首页
    '''

    def response(self):
        self.finish()
