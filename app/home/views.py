#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from app import app
from flask import request, redirect, render_template
# from app.models import Product, Shop, Detail, Presell
from . import blueprint
import json
import time
from app.wechat.wxapi import WxPayConf_pub
from  app.wechat.wxapi.backends.fl import Helper

@blueprint.route('/')
def hello_world():
    return 'Hello World!'

@blueprint.route('/zhangjuan')
def hello_world1111():
    return 'Hello sjdfjsdfjsjdfjsdf!'


@blueprint.route('/index', methods=['GET'])
def web_index():
    print('index')
    return redirect('/static/web_video/index.html')


def test():
    #print(web.weixin.access_token_info)
    return render_template('weixin.html')


def h5_1():
    return render_template('h5/1/index.html')


def h5_2():
    return flask.render_template('h5/2/index.html')


@blueprint.route('/presell', methods=['GET', 'POST'])
def presell():
    #curl -X POST -d "username=my&phone=12345" 0.0.0.0:4000/presell
    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        presells = Presell.objects()
        pg = presells.paginate(page=page, per_page=10)  # Shop.objects.delete()
        return render_template('presell.html', presells=pg)

    if request.method == 'POST':
        print(request.form)

        username = str(request.form.get('username', ''))
        phone = str(request.form.get('phone', ''))
        print(username, phone)
        if username and phone:
            presell = Presell(username=username, phone=phone)
            presell.save()
            return 'yes'
        return 'no'



ERROR = ['没有数据']


def rates(pid=None):
    p = None
    r = None
    p = Product.objects(pid=str(pid)).first()
    if p:
        r = Detail.objects.filter(product=p).first()
    if r:
        r = r.rate.split('\n')
    else:
        r = ERROR
    return render_template('rates.html', rates=r)


def deal(pid=None):
    p = None
    r = None
    p = Product.objects(pid=str(pid)).first()
    if p:
        r = Detail.objects.filter(product=p).first()
    if r:
        r = r.deal.split('\n')
    else:
        r = ERROR
    return render_template('deal.html', deal=r)


def detail(pid=None):
    p = None
    r = None
    p = Product.objects(pid=str(pid)).first()
    if p:
        r = Detail.objects.filter(product=p).first()
    if r:
        temp = r.price.split('\n')
        temp += r.detail.split('\n')
    else:
        temp = ERROR
    return render_template('detail.html', detail=temp)


def index():

    page = int(request.args.get('page', 1))
    ps = Product.objects()
    pg = ps.paginate(page=page, per_page=10)  # Shop.objects.delete()

    return render_template('index.html', qsp=pg)

#import test_gevent

#def get_data():
#    test_gevent.pool_test('小米 空气进化器', 1000, pages=1)

@app.route('/testing_app1/addEquipment')
def addEquipment():
    return render_template('testing_app1/addEquipment.html')

@app.route('/testing_app1/equipment')
def equipment():
    return render_template('testing_app1/equipment.html')

#
@app.route('/testing_app1/equipmentIndex',methods=["GET","POST"])
def equipmentList():
    if request.method == 'GET':
        # 如果用户的数据库里有产品的话,直接重定向为/testing_app1/equipment
        #步骤1:获取用户openid,
        #步骤2:匹配用户数据库,找出拥有的产品资料库
        #步骤3:判断产品资料库是否为空
        userProduct = []
        # userProduct = "nihjai"
        if(userProduct):
            return redirect("/testing_app1/equipment")
        else:
            url = request.url
            print(url)
            sign = Helper.jsapi_sign(url)
            sign["appId"] = WxPayConf_pub.APPID
            # sign = {}
            # sign["appId"] = "123"
            return render_template('testing_app1/equipmentList.html',sign=sign)

    if request.method == 'POST':
        print(request.form)
        codeResult = str(request.form.get('codeResult', ''))
        print(codeResult)
        if codeResult:
            return 'yes'
        return 'no'

# 设备设置
@app.route('/testing_app1/install')
def install():
    return render_template('testing_app1/install_index.html')
# 产品介绍
@app.route('/testing_app1/introduce')
def introduce():
    return render_template('testing_app1/introduce.html')

@app.route('/testing_app1/net')
def net():
    someday = {"work":86,"no_work":21}
    return render_template('testing_app1/net.html',someday=someday)

@app.route('/testing_app1/netList')
def netList():
    #从用户产品数据库,取出所拥有的产品id,名称以及图片路径
    orderJson = [{'productId':4534,'proName':"兆晶新风机(卧室)","proImgUrl":"app/img/equip.png"},{'productId':6789,'proName':"兆晶新风机(客厅)","proImgUrl":"app/img/netImg.jpg"},{'productId':1190,'proName':"兆晶新风机(客厅)","proImgUrl":"app/img/netImg.jpg"}]
    return render_template('testing_app1/netList.html',orderJson=orderJson)

#订单查询
@app.route('/testing_app1/order',methods=['GET', 'POST'])
def order():
    # orderJson = [{'orderNum':453499,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新风x100","adapterodel":"sdhh水电费","quantity":1,"sumMoney":360},{'orderNum':11111111,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':222222,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':33333333,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':4444444,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':555555,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':666666,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':777777,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':8888888,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':999999,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':100000,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540}]
    orderJson = {}
    print(len(orderJson))
    page={} #判断数据库是否有数据,有数据的话,page2显示,否则page1显示
    if orderJson:
        page["page1"] = ""
        page["page2"] = "page-current"
    else:
        page["page1"] = "page-current"
        page["page2"] = ""

    lenList = {}
    lenList["sumLen"]=len(orderJson)  #数据库的总条数
    lenList["preLen"]=4     #每次添加条数
    if lenList["sumLen"] <= lenList["preLen"]:
        lenList["Len"] = lenList["sumLen"]
    else:
        lenList["Len"] = lenList["preLen"]

    if request.method == 'GET':
        return render_template('testing_app1/order.html',orderJson=orderJson,lenList=lenList,page=page)

    if request.method == 'POST':
        print(request.form)
        # 获取已经显示的条数,以及下标
        lastIndex = int(request.form.get('lastIndex', ''))
        print(lastIndex)
        if lastIndex + lenList["preLen"] > lenList["sumLen"]:
            nowLen = lenList["sumLen"]
        else:
            nowLen = lastIndex + lenList["preLen"]

        orderData = orderJson[lastIndex:nowLen]
        print(orderData)
        return json.dumps(orderData)


# 之前的订单详情
@app.route('/testing_app1/orderdetail')
def orderdetail():
    # 从cookie得到订单号
    orderNum = request.cookies.get('orderNum')
    print(orderNum)
    # 由订单号匹配,在订单数据库,取出相应的数据
    orderings = {}
    orderings["netId"] = "990"  #滤网id
    orderings["price"] = 100   #滤网单价
    orderings["quantity"] = 1  #购买数量
    orderings["sendWay"] = "包邮"  #配送方式
    orderings["name"] = "李大建"  #收货人
    orderings["tel"] = "11352146590"   #收货电话
    orderings["address"] = "广东省广州市天河区林和西路9号耀中广场B座910-911室"  #收货地址
    orderings["time"] = "2015-09-12 11:67"  #下单时间
    orderings["message"] = ""  #留言内容
    orderings["amount"] = 100  #总金额
    # 由滤网id匹配,在滤网数据库,取出相应数据
    netData = {}
    netData["netImg"] = "app/img/netImg.jpg"  #滤网图片url
    netData["pro_name"] = "高效过滤网"  #滤网名称
    netData["pro_type"] = "适配x100"   #滤网适配类型
    return render_template('testing_app1/orderDetail.html',orderings=orderings,netData=netData)

#下订单的详情
@app.route('/testing_app1/ordering')
def ordering():
    net_proId = request.cookies.get('net_proId')
    print(net_proId)
    # 根据从cookie得到产品的id,匹配相对应的滤网id,从滤网取出数据
    netData = {}
    netData["netId"] = "990"  #滤网的id
    netData["netImg"] = "app/img/netImg.jpg"  #滤网的图片url
    netData["pro_name"] = "高效过滤网"  #滤网名称
    netData["pro_type"] = "适配x100"   #滤网适配类型说明
    netData["price"] = "100"   #滤网单价
    netData["sendWay"] = "包邮"   #滤网配送方式
    # 获取用户的信息
    userMessage = {}
    userMessage["name"] = "李大建"   #用户名
    userMessage["tel"] = "11352146590"  #用户联系电话
    userMessage["address"] = "广东省广州市天河区林和西路9号耀中广场B座910-911室"  #用户地址
    return render_template('testing_app1/ordering.html',netData=netData,userMessage=userMessage)

@app.route('/testing_app1/personal')
def personal():
    return render_template('testing_app1/personal.html')

@app.route('/testing_app1/setingTime')
def setingTime():
    return render_template('testing_app1/setingTime.html')

@app.route('/testing_app1/setParameter')
def setParameter():
    return render_template('testing_app1/setParameter.html')

@app.route('/testing_app1/setTime')
def setTime():
    return render_template('testing_app1/setTime.html')

@app.route('/testing_app1/setup')
def setup():
    return render_template('testing_app1/setup.html')

# 滤网使用时间,我觉得这里可以进行修改,不需要前端发送ajax
# @blueprint.route('/netTime', methods=['GET', 'POST'])
# def netTime1():
#     objJson = {'usedTime':66,'remainTime':21}
#     if request.method == 'GET':
#          return json.dumps(objJson)
#     if request.method == 'POST':
#         return json.dumps(objJson)

# order
# @blueprint.route('/order', methods=['GET', 'POST'])
# def order():
#     orderJson = {'orderNum':4534,'tradingStatus':"交易成功","netImgUrl":"static/app/img/netImg.jpg","netName":"兆晶新风x100","adapterodel":"sdhh水电费","quantity":1,"sumMoney":360},{'orderNum':4456534,'tradingStatus':"交易成功","netImgUrl":"static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540}
#     if request.method == 'GET':
#          return json.dumps(orderJson)
#     if request.method == 'POST':
#         return json.dumps(orderJson)

# netList
# @blueprint.route('/netList', methods=['GET', 'POST'])
# def netList_h():
#     orderJson = {'productId':4534,'proName':"兆晶新风机(卧室)","proImgUrl":"/static/app/img/equip.png"},{'productId':6789,'proName':"兆晶新风机(客厅)","proImgUrl":"/static/app/img/netImg.jpg"}
#     if request.method == 'GET':
#          return json.dumps(orderJson)
#     if request.method == 'POST':
#         return json.dumps(orderJson)

# 订单生成,详细信息
@blueprint.route('/orderingDetail', methods=['GET', 'POST'])
def orderingDetail():
    if request.method == 'POST':
        print(request.form)
        orderings = {}
        # 这里是返回数据的收集
        orderings["netId"] = str(request.form.get('netId', ''))  #滤网id
        orderings["price"] = str(request.form.get('price', ''))  #滤网单价
        orderings["quantity"] = str(request.form.get('quantity', ''))  #购买滤网的数量
        orderings["sendWay"] = str(request.form.get('sendWay', ''))  #配送方式
        orderings["name"] = str(request.form.get('name', ''))  #收货人
        orderings["tel"] = str(request.form.get('tel', ''))  #收货人电话号码
        orderings["address"] = str(request.form.get('address', ''))  #收货地址
        orderings["time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #当前时间
        orderings["message"] = str(request.form.get('message', ''))  #留言内容
        orderings["amount"] = str(request.form.get('amount', ''))  #总金额
        print(orderings)
        if orderings:
            return 'yes'
        return 'no'


# 异常提醒(获得)
@blueprint.route('/abnormalWarn', methods=['GET', 'POST'])
def abnormalWarn1():
    if request.method == 'POST':
        print(request.form)
        abnormalId = str(request.form.get('id'))
        print(abnormalId)
        abnormalData1 = {"id":abnormalId,"select":"true"}
        return json.dumps(abnormalData1)
        # return request.form.get('select')
        # return request.form.get('select');

# 更新滤网提醒
@blueprint.route('/netChangeW', methods=['GET', 'POST'])
def netChangeW():
    if request.method == 'POST':
        print(request.form)
        select = str(request.form.get('select'))
        abnormalId = str(request.form.get('id'))
        print(select + abnormalId)
        return "hello"
        # return request.form.get('select')
        # return request.form.get('select');

#获取已设置的时间 开机时间
@blueprint.route('/openTimeList', methods=['GET', 'POST'])
def openTimeList():
    if request.method == 'POST':
        ss = ""

        # 判断数据库中有没有时间的数据,
        if(ss):
            return ss


#获取已设置的时间 关机时间
@blueprint.route('/closeTimeList', methods=['GET', 'POST'])
def closeTimeList():
    if request.method == 'POST':
        return "sdf"


#设置时间 开机时间
@blueprint.route('/setingOpen', methods=['GET', 'POST'])
def setingOpen():
    if request.method == 'POST':
        print(request.form)
        time = str(request.form.get('time'))
        recur = str(request.form.get('recur'))
        print(time + recur)
        return "yes"

#设置时间 关机时间
@blueprint.route('/setingClose', methods=['GET', 'POST'])
def setingClose():
    if request.method == 'POST':
        print(request.form)
        time = str(request.form.get('time'))
        recur = str(request.form.get('recur'))
        print(time + recur)
        return "yes"


#设置参数
@blueprint.route('/getParameter', methods=['GET', 'POST'])
def getParameter():
    if request.method == 'POST':
        # 返回的数据包含:最大值,最小值,最适宜或者用户设置的(一共3*3=9个)

        parameter = {"temper":{"temMax":35,"temMin":16,"temfit":25},"damp":{"dampMax":90,"dampMin":0,"dampfit":60},"co2":{"co2Max":35,"co2Min":16,"co2fit":25}}
        return json.dumps(parameter)

#获取参数
@blueprint.route('/setParameter', methods=['GET', 'POST'])
def setParameter():
    if request.method == 'POST':
        print(request.form)
        temfit = str(request.form.get('temfit'))
        dampfit = str(request.form.get('dampfit'))
        co2fit = str(request.form.get('co2fit'))

        # 覆盖到用户设置的参数表中

        return "yes"

# 设置电话和地址
@blueprint.route('/getPersonal', methods=['GET', 'POST'])
def getPersonal():
    if request.method == 'POST':
        perInfor = {"headUrl":"static/app/img/netImg.jpg","nickName":"zhangjuan","machine":2,"yourTel":"13580467147","addressCity":"广东 广州 天河区","fullAddress":"林和西路耀中广场B座910"}
        return json.dumps(perInfor)

