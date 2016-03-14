# -*- coding: utf-8 -*-
#from .. import app
from flask import g
from flask import request, Response, render_template

from .wxapi import handler as HD
from .wxapi.backends.fl import (Helper, sns_userinfo_callback)
from .wxapi.lib import WeixinHelper
from .wxapi.config import WxPayConf_pub
from . import app
#
# @blueprint.route('/do', methods=['GET', 'POST'])
# def do():
#     """公众平台对接"""
#     signature = request.args.get("signature", "")
#     timestamp = request.args.get("timestamp", "")
#     nonce = request.args.get("nonce", "")
#     if not any([signature, timestamp, nonce
#                 ]) or not WeixinHelper.checkSignature(signature, timestamp,
#                                                       nonce):
#         return Response("check failed")
#
#     if request.method == "GET":
#         return Response(request.args.get("echostr"))
#     elif request.method == "POST":
#         #print request.raw_post_data
#         handler = HD.MessageHandle(request.data)
#         response = handler.start()
#         return Response(response)
#     else:
#         return Response("")
#
#
# @HD.subscribe
# def subscribe(xml):
#     """关注事件"""
#     return "welcome to weixin-knife"
#
#
# @HD.unsubscribe
# def unsubscribe(xml):
#     """取关事件"""
#     print("leave weixin-knife")
#     return "leave"
#
#
# @HD.text
# def text(xml):
#     """文本消息"""
#     content = xml.Content
#     if content == "111":
#         return {
#             "Title": "美女",
#             "Description": "比基尼美女",
#             "PicUrl":
#             "http://9smv.com/static/mm/uploads/150411/2-150411115450247.jpg",
#             "Url": "http://9smv.com/beauty/list?category=5"
#         }
#     elif content == "222":
#         return [
#             ["比基尼美女", "比基尼美女",
#              "http://9smv.com/static/mm/uploads/150411/2-150411115450247.jpg",
#              "http://9smv.com/beauty/list?category=5"],
#             ["长腿美女", "长腿美女",
#              "http://9smv.com/static/mm/uploads/150506/2-150506111A9648.jpg",
#              "http://9smv.com/beauty/list?category=8"]
#         ]
#     return "hello world"
#
#
# def userinfo_process(openid, userinfo):
#     print(openid, userinfo)
#
#
# @blueprint.route('/oauth', methods=['GET', 'POST'])
# @sns_userinfo_callback(userinfo_process)
# def oauth():
#     """网页授权获取用户信息"""
#     resp = Response(g.openid)
#     resp.set_cookie('openid', Helper.sign_cookie(g.openid))
#     return resp
#
#
# @blueprint.route('/favicon.ico', methods=['GET', 'POST'])
# def favicon():
#     return ''
#
#
# @blueprint.route('/saoyisao/<path:template>', methods=['GET', 'POST'])
# def share(template=None):
#     print(template)
#     url = request.url
#     print(url)
#     sign = Helper.jsapi_sign(url)
#     sign["appId"] = WxPayConf_pub.APPID
#     print(sign)
#     return render_template(template, sign=sign)

@app.route('/')
def helo():
    return "hello"


@app.route('/saoyisao/')
@app.route("/saoyisao/<path:template>")
def hello(template=None):
    url = request.url
    print(url)
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    return render_template(template,sign=sign)
