#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from app import app
from flask import request, redirect, render_template
from app.models import Product, Shop, Detail, Presell
from . import blueprint
import json
import time
from app.wechat.wxapi import WxPayConf_pub
from  app.wechat.wxapi.backends.fl import Helper
from app.wechat.wxapi import JsApi_pub,UnifiedOrder_pub,WxPayConf_pub

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


#测试首页
@app.route('/testing_app1/wxIndex')
def wxIndex():
    return render_template('testing_app1/wxIndex.html')

#设备进入
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

#二维码扫描或wifi成功进入
@app.route('/testing_app1/addEquipment',methods=["GET","POST"])
def addEquipment():
    if request.method == 'GET':
        machineIdName = [{'productId':4534},{'productId':6789},{'productId':1190}]
        return render_template('testing_app1/addEquipment.html',machineIdName=machineIdName)
    if request.method == 'POST':
        print(request.form)
        # 将获得的数据产品的ID,添加到绑定设备的列表里,绑定设备的列表需要有产品的ID和产品图片.
        return ""

#已绑定的设备列表
@app.route('/testing_app1/equipment')
def equipment():
    #从用户产品数据库,取出所拥有的产品id,名称以及图片路径,控制者
    machineJson = [{'productId':4534,'proName':"兆晶新风机(卧室)","proImgUrl":"app/img/equip.png","controller":"李霞"},
                   {'productId':6789,'proName':"兆晶新风机(客厅)","proImgUrl":"app/img/equip.png","controller":"李大健"},
                   {'productId':1190,'proName':"兆晶新风机(客厅)","proImgUrl":"app/img/equip.png","controller":"李霞"}]
    url = request.url
    print(url)
    sign = Helper.jsapi_sign(url)
    sign["appId"] = WxPayConf_pub.APPID
    return render_template('testing_app1/equipment.html',machineJson=machineJson,sign=sign)

# 设备操作
@app.route('/testing_app1/install', methods=['GET', 'POST'])
def install():
    if request.method == 'GET':
        productId = request.cookies.get('productId')
        # 获取productId下面的产品设置的信息
        # 如果onOff=true,那么就是设备开启,需要设置是什么模式,如果为false那么就是自动模式
        machineModel = {'productId':productId,"onOff":"true",'model':"睡眠","temperOut":"25","temperRoom":"32","dampOut":"45","dampRoom":"60",
                        'PMOut':"20","PMRoom":"200","netTime":"20","position":"广州","airQuality":"良","airPosition":"伦敦","locationImg":"app/img/lendon.png"}
        # print(machineModel)
        return render_template('testing_app1/install_index.html',machineModel = machineModel)
    if request.method == 'POST':
        # 注意这是第几个设备,有productId.
        # 将返回来的数据放到数据库中,更新onOff,model,并且设备设置成返回的数据的模式,还有开设备还是关设备
        print(request.form)
        return ""

# 一键滤网
@app.route('/testing_app1/net')
def net():
    someday = {"work":86,"no_work":21}
    return render_template('testing_app1/net.html',someday=someday)

#滤网列表
@app.route('/testing_app1/netList')
def netList():
    #从用户产品数据库,取出所拥有的产品id,名称以及图片路径
    orderJson = [{'productId':4534,'proName':"兆晶新风机(卧室)","proImgUrl":"app/img/equip.png"},{'productId':6789,'proName':"兆晶新风机(客厅)","proImgUrl":"app/img/netImg.jpg"},{'productId':1190,'proName':"兆晶新风机(客厅)","proImgUrl":"app/img/netImg.jpg"}]
    return render_template('testing_app1/netList.html',orderJson=orderJson)

#下订单
@app.route('/testing_app1/ordering/',methods=["GET","POST"])
def ordering():
    if request.method == 'GET':
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

        url = request.url
        print(url)
        sign = Helper.jsapi_sign(url)
        sign["appId"] = WxPayConf_pub.APPID
        return render_template('testing_app1/ordering.html',netData=netData,userMessage=userMessage,sign=sign)
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
        out_trade_no = "1728488032176388"
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
        # Parameters = json.loads(jsApiParameters)
        print(jsApiParameters)
        return jsApiParameters


# 个人
@app.route('/testing_app1/personal', methods=['GET', 'POST'])
def personal():
    if request.method == 'GET':
        perInfor1 = {"headUrl":"app/img/netImg.jpg","nickName":"zhangjuan","machine":2,"yourTel":"13580467147",
                 "addressCity":"广东 广州 天河区", "fullAddress":"林和西路耀中广场B座910"}
        return render_template('testing_app1/personal.html',perInfor1 = perInfor1)
    if request.method == 'POST':
            print(request.form)
            yourTel = str(request.form.get('yourTel'))
            addressCity = str(request.form.get('addressCity'))
            fullAddress = str(request.form.get('fullAddress'))
            # 放到个人列表中,有电话号码,省市区,详细地址
            # 可以比较三个值中的数据和返回过来的数据有没有差别,如果有就更新到数据库中
            return ""

# 设置
@app.route('/testing_app1/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'GET':
        abnormalData1 = {"id":"renew","select":"true"},{"id":"unusual","select":"false"}
        return render_template('testing_app1/setup.html',abnormalData1 = abnormalData1)
    if request.method == 'POST':
        print(request.form)
        # 更换滤网提醒与异常提醒
        # 异常id : unusual ,当select为false,不提示
        # 更换滤网提醒id : renew ,当select为false,不提示
        id = str(request.form.get('id'))
        select = str(request.form.get('select'))
        # 存到数据库中
        return ""

# 产品介绍
@app.route('/testing_app1/introduce')
def introduce():
    return render_template('testing_app1/introduce.html')

#设置时间
@app.route('/testing_app1/setTime', methods=['GET', 'POST'])
def setTime():
    if request.method == 'GET':
         # 开机时间和关机时间
        # openTime = [{"onTime":"17:35","betweenTimeH":"1","betweenTimeM":"15","repeatTime":"仅一次","Tselect":"false"},{"onTime":"17:35","betweenTimeH":"1","betweenTimeM":"15","repeatTime":"仅一次","Tselect":"false"}]
        getTime = {"openTime":{"onTime":"17:35","betweenTimeH":"1","betweenTimeM":"15","repeatTime":"仅一次","Tselect":"false"},
                   "closeTime":{"offTime":"17:35","betweenTimeH":"1","betweenTimeM":"15","repeatTime":"重复","Tselect":"true"}}
        print(getTime)
        return render_template('testing_app1/setTime.html',getTime = getTime)

    # 是否开启开关机时间
    if request.method == 'POST':
        print(request.form)
        timeId = str(request.form.get('timeId'))
        Tselect = str(request.form.get('Tselect'))
        # timeId是开机时间还是关机时间,如果timeId的值为openTimeList就是开机,否则为关机
        # 此处需要放到数据库中的是Tselect的值,将Tselect的值更改到开机或者关机的表里(具体放到开机还是关机根据timeId定)
        return ""

#正在设置时间
@app.route('/testing_app1/setingTime',methods=['GET', 'POST'])
def setingTime():
    if request.method == 'GET':
        return render_template('testing_app1/setingTime.html')
    if request.method == 'POST':
        print(request.form)
        #根据timeType判断,是openTime,则设置的是开机时间,否是关机时间
        timeType = str(request.form.get('timeType'))
        time = str(request.form.get('time'))
        recur = str(request.form.get('recur'))
        # 将time存到开机时间的offTime里
        # recur 记录重复的天数,也要放进去,
        return ""



#获取参数
@app.route('/testing_app1/setParameter', methods=['GET', 'POST'])
def setParameter():
    if request.method == 'GET':
        # 返回的数据包含:最大值,最小值,最适宜或者用户设置的(一共3*3=9个)
        parameter = {"temper":{"temMax":35,"temMin":16,"temfit":25},
                     "damp":{"dampMax":90,"dampMin":0,"dampfit":60},
                     "co2":{"co2Max":35,"co2Min":16,"co2fit":25}}
        return render_template('testing_app1/setParameter.html',parameter=parameter)
    if request.method == 'POST':
        print(request.form)
        temfit = str(request.form.get('temfit'))
        dampfit = str(request.form.get('dampfit'))
        co2fit = str(request.form.get('co2fit'))
        # 覆盖到用户设置的参数表中
        return "yes"


#订单查询
@app.route('/testing_app1/order',methods=['GET', 'POST'])
def order():
    orderJson = [{'orderNum':453499,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新风x100","adapterodel":"sdhh水电费","quantity":1,"sumMoney":360},{'orderNum':11111111,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':222222,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':33333333,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':4444444,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':555555,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':666666,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':777777,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':8888888,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':999999,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540},{'orderNum':100000,'tradingStatus':"交易成功","netImgUrl":"/static/app/img/netImg.jpg","netName":"兆晶新55风x100","adapterodel":"sdhh水555电费","quantity":1,"sumMoney":3540}]
    # orderJson = {}
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



