#coding=utf8
'''
Created on 2014-5-19
flask 帮助函数

@author: skycrab

flask 没有提供Helper函数，可以仿照django的Helper实现

@app.route('/login', methods=['GET', 'POST'])
@sns_userinfo
def oauth():
    openid = g.openid

'''

import json
from functools import wraps

from werkzeug.contrib.cache import SimpleCache
from flask import request, redirect, g
from flask import current_app as app

from .. import class_property, WeixinHelper
from .common import CommonHelper

cache = SimpleCache()


class Helper(CommonHelper):
    """微信具体逻辑帮组类"""

    @class_property
    def cache(cls):
        """返回cache对象"""
        return cache

    @class_property
    def secret_key(cls):
        """返回cookie加密秘钥"""
        return app.config['SECRET_KEY']


def sns_userinfo_callback(callback=None):
    """网页授权获取用户信息装饰器
    callback(openid, userinfo):
        return user
    """

    def wrap(func):
        @wraps(func)
        def inner(*args, **kwargs):
            openid = request.cookies.get('openid')
            userinfo = None
            if not openid:
                code = request.args.get("code")
                if not code:
                    return redirect(WeixinHelper.oauth2(request.url))
                else:
                    data = json.loads(WeixinHelper.getAccessTokenByCode(code))
                    access_token, openid, refresh_token = data[
                        "access_token"], data["openid"], data["refresh_token"]
                    #WeixinHelper.refreshAccessToken(refresh_token)
                    userinfo = json.loads(WeixinHelper.getSnsapiUserInfo(
                        access_token, openid))
            else:
                ok, openid = Helper.check_cookie(openid)
                if not ok:
                    return redirect("/")
            g.openid = openid
            if callable(callback):
                g.user = callback(openid, userinfo)
            response = func()
            return response

        return inner

    return wrap


sns_userinfo = sns_userinfo_callback()

# 自己加上去
def ans_base(callback=None):
    def wrap(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # openid = request.cookies.get('openid')
            # userinfo = None
            # if not openid:
            code = request.args.get("code")
            if not code:
                return redirect(WeixinHelper.oauth2_base(request.url))
            #     else:
            #         data = json.loads(WeixinHelper.getAccessTokenByCode(code))
            #         openid = data["openid"]
            #         userinfo = json.loads(WeixinHelper.getSnsapiUserInfo(
            #             access_token, openid))
            #         # userinfo = {"status":"yes"}
            # else:
            #     ok, openid = Helper.check_cookie(openid)
            #     if not ok:
            #         return redirect("/")
            # g.openid = openid
            # if callable(callback):
            #     # status = "yes"
            #     g.user = callback(openid, userinfo)
            # response = func()
            # return response
            return func(*args, **kwargs)

        return inner

    return wrap
