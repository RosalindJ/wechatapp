# -*- coding: utf-8 -*-
#from .. import app
from flask import g
from flask import request, Response, render_template,redirect

from .wxapi import handler as HD
from .wxapi.backends.fl import (Helper, sns_userinfo)
from .wxapi.lib import WeixinHelper
from .wxapi.config import WxPayConf_pub
from . import app
from .wxapi.pay import JsApi_pub
from .wxapi.testpay import jsApiParameters

@app.route('/do', methods=['GET', 'POST'])
def do():
    """公众平台对接"""
    signature = request.args.get("signature", "")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    if not any([signature, timestamp, nonce
                ]) or not WeixinHelper.checkSignature(signature, timestamp,
                                                      nonce):
        return Response("check failed")

    if request.method == "GET":
        return Response(request.args.get("echostr"))
    elif request.method == "POST":
        #print request.raw_post_data
        handler = HD.MessageHandle(request.data)
        response = handler.start()
        return Response(response)
    else:
        return Response("")


@HD.subscribe
def subscribe(xml):
    """关注事件"""
    return "welcome to weixin-knife"


@HD.unsubscribe
def unsubscribe(xml):
    """取关事件"""
    print("leave weixin-knife")
    return "leave"


@HD.text
def text(xml):
    """文本消息"""
    content = xml.Content
    if content == "111":
        return {
            "Title": "美女",
            "Description": "比基尼美女",
            "PicUrl":
            "http://9smv.com/static/mm/uploads/150411/2-150411115450247.jpg",
            "Url": "http://9smv.com/beauty/list?category=5"
        }
    elif content == "222":
        return [
            ["比基尼美女", "比基尼美女",
             "http://9smv.com/static/mm/uploads/150411/2-150411115450247.jpg",
             "http://9smv.com/beauty/list?category=5"],
            ["长腿美女", "长腿美女",
             "http://9smv.com/static/mm/uploads/150506/2-150506111A9648.jpg",
             "http://9smv.com/beauty/list?category=8"]
        ]
    return "hello world"


def userinfo_process(openid, userinfo):
    print(openid, userinfo)


@app.route('/oauth', methods=['GET', 'POST'])
@sns_userinfo
def oauth():
    """网页授权获取用户信息"""
    resp = Response(g.openid)
    print(g.openid)
    resp.set_cookie('openid', Helper.sign_cookie(g.openid))
    return resp


@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return ''


@app.route('/share/<path:template>', methods=['GET', 'POST'])
def share(template=None):
    print(template)
    url = request.url
    print(url)
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    print(sign)
    return render_template(template, sign=sign)

@app.route('/')
def hello():
    return "hello"


# 调用微信扫一扫,返回签名等
# @app.route("/saoyisao/<path:template>")
# def apiSign(template=None):
#     url = request.url
#     print(url)
#     sign = {}
#     sign["appId"] = "123"
#     sign["timestamp"] = 123
#     return render_template(template,sign=sign)

@app.route("/saoyisao/<path:template>")
def saoyisao(template=None):
    url = request.url
    print(url)
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    return render_template(template,sign=sign)

#二维码扫出的结果接受
@app.route("/codeResult",methods=['GET','POST'])
def code():
    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        print(page)

    if request.method == 'POST':
        print(request.form)
        codeResult = str(request.form.get('codeResult', ''))
        print(codeResult)
        if codeResult:
            return 'yes'
        return 'no'

# 微信支付
@app.route("/wxpay/<path:template>")
def wxpay(template=None):
    url = request.url
    print(url)
    redirect(WeixinHelper.oauth2_base(url))
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    print(sign)
    # parameters = jsApiParameters.getJsParameters()
    # print(parameters)
    parameters = {}
    parameters["nonceStr"] = "123"
    # parameters["timestamp"] = 123
    return render_template(template,sign=sign,parameters=parameters)

# @app.route("/wxpay/<path:template>")
# def wxpay(template=None):
#     url = request.url
#     print(url)
#     sign = {}
#     sign["appId"] = "123"
#     sign["timestamp"] = 123
#     # parameters = {}
#     # parameters["nonceStr"] = "123"
#     # parameters["timestamp"] = 123
#     parameters = JsApi_pub.getParameters()
#     print(parameters)
#     return render_template(template,sign=sign,parameters=parameters)