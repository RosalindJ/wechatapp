# -*- coding: utf-8 -*-
#from .. import app
from flask import request, Response, render_template,redirect
from flask import g

from .wxapi import handler as HD
from .wxapi.backends.fl import (Helper, sns_userinfo,sns_userinfo_callback)
from .wxapi import (WeixinHelper, WxPayConf_pub)

from . import blueprint


@blueprint.route('/do', methods=['GET', 'POST'])
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


@blueprint.route('/oauth', methods=['GET', 'POST'])
@sns_userinfo
# @sns_userinfo_callback(userinfo_process)
def oauth():
    """网页授权获取用户信息"""
    resp = Response(g.openid)
    print(g.openid)
    resp.set_cookie('openid', Helper.sign_cookie(g.openid))
    return resp


@blueprint.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return ''


@blueprint.route('/share/<path:template>', methods=['GET', 'POST'])
def share(template=None):
    print(template)
    url = request.url
    print(url)
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    print(sign)
    return render_template(template, sign=sign)



import time
from app.wechat.wxapi import JsApi_pub,UnifiedOrder_pub,WxPayConf_pub
import json
# 自己加上去的 测试支付使用的
@blueprint.route('/oauth_base/', methods=['GET', 'POST'])
# @sns_userinfo
def oauth_base():
    """网页授权获取用户信息"""
    # resp = Response(g.openid)
    # print(g.openid)
    # resp.set_cookie('openid', Helper.sign_cookie(g.openid))

    unifiedOrder = UnifiedOrder_pub()
    # 用户标识
    unifiedOrder.setParameter("openid","oIJFBwhI__1d-BRuJPs8ubS81KyI")
    # unifiedOrder.setParameter("openid",resp)
    # 商品描述
    unifiedOrder.setParameter("body","hello")
    # 订单号自定义,此处举例
    # timeStamp = str(time.time())
    # print(timeStamp)
    out_trade_no = "1728488032176111"
    unifiedOrder.setParameter("out_trade_no",out_trade_no)
    # 总金额
    unifiedOrder.setParameter("total_fee","1")
    # 收货地址,这里的NOTIFY——URL根据需要是否使用共享收货地址而定
    unifiedOrder.setParameter("notify_url",WxPayConf_pub.NOTIFY_URL)
    # 交易类型
    unifiedOrder.setParameter("trade_type","JSAPI")
    prepay_id = unifiedOrder.getPrepayId()

    JsApi = JsApi_pub()
    JsApi.setPrepayId(prepay_id)
    jsApiParameters = JsApi.getParameters()
    Parameters = json.loads(jsApiParameters)
    print(Parameters)

    url = request.url
    print(url)
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    return render_template("pay/base_openid.html",jsApiParameters=Parameters,sign=sign)

# 测试微信回调使用的
from app.wechat.wxapi import Notify_pub
from app.wechat.wxapi.log import Log_
@blueprint.route('/notify_url/', methods=['GET', 'POST'])
def notify_url():
    #使用通用通知接口
    notify = Notify_pub()

    #存储微信的回调
    xml = request.form #$GLOBALS['HTTP_RAW_POST_DATA']
    print(xml)
    notify.saveData(xml)

    #验证签名，并回应微信
    #对后台通知交互时，如果微信收到商户的应答不是成功或超时，微信认为通知失败，
    #微信会通过一定的策略（如30分钟共8次）定期重新发起通知
    #尽可能提高通知的成功率，但微信不保证通知最终能成功。
    if notify.checkSign() == False :
        notify.setReturnParameter("return_code","FAIL")
        notify.setReturnParameter("return_msg","签名失败")
    else:
        notify.setReturnParameter("return_code","SUCCESS")

    returnXml = notify.returnXml()
    print(returnXml)

    #商户根据实际情况设置相应的处理流程，此处仅作举例
    #以log文件形式记录回调信息
    log = Log_()
    log_name = "./notify_url.log" #log文件路径
    log.log_result(log_name,"[接收到的notify通知]:\n"+xml+"\n")
    if notify.checkSign() == True:
        if notify.data["return_code"] == "FAIL":
            log.log_result(log_name,'[通信出错]:\n'+xml+"\n")
        elif notify.data["result_code"] == "FAIL":
            log.log_result(log_name,'[业务出错]:\n'+xml+"\n")
        else:
            log.log_result(log_name,"[支付成功]:\n"+xml+"\n")


        #商户自行增加处理流程
        #例如：更新订单状态
        #例如：数据库操作
        #例如：推送支付完成信息

    return ""





