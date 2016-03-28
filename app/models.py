import datetime
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()


class Shop(db.Document):
    sid = db.StringField(max_length=40)
    href = db.URLField()


class Product(db.Document):
    pid = db.StringField(max_length=40)
    href = db.URLField()
    keywords = db.StringField()
    shop = db.ReferenceField(Shop)

class Detail(db.Document):
    product = db.ReferenceField(Product)
    rate = db.StringField()
    detail = db.StringField()
    price = db.StringField()
    deal = db.StringField()


class Presell(db.Document):
    username = db.StringField()
    phone = db.StringField()
    created_time = db.DateTimeField(default=datetime.datetime.now)


#用户信息
class Users(db.Document):
    openid = db.StringField(unique=True, required=True)#用户opeoid
    nickname = db.StringField()#用户名称
    headimgurl = db.URLField()#用户头像url
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间

    meta = {
        'collection':'users'
    }


# 设备基本配置信息
class Devices(db.Document):
    pid = db.StringField(unique=True, required=True)#设备ID
    name = db.StringField()#设备名称
    pname = db.StringField()#生产厂商名称
    p_active = db.BooleanField(default=False)#出厂激活
    p_active_time = db.DateTimeField()#出厂激活时间
    c_active = db.BooleanField(default=False)#用户激活
    c_active_time = db.DateTimeField()#用户激活时间
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#创建时间
    meta = {
        'collection':'devices'

    }

#设备网络配置信息
class DevicesNetworkConfigure(db.Document):
    device = db.ReferenceField(Devices)#设备
    ssid = db.StringField()#wifi ssid
    server_addr = db.StringField()#服务器地址
    mac_addr = db.StringField()#设备MAC地址
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#创建时间
    meta = {
        'collection':'devices_network_configure'

    }

class DevicesSwitchConfigure(db.Document):
    device = db.ReferenceField(Devices)#设备

    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#创建时间
    meta = {
        'collection':'devices_switch_configure'

    }

#设备运行配置信息
class DevicesSetupConfigure(db.Document):
    device = db.ReferenceField(Devices)#设备
    name = db.StringField()#配置名称
    temprature_limit = db.IntField()#温度限制
    moisture_limit = db.IntField()#湿度限制
    co2_limit = db.IntField()#CO2限制
    pm25_limit = db.IntField()#PM25限制
    formalde_limit = db.IntField()#甲醛限制
    secure_level = db.StringField()#安全限制
    mode = db.StringField()#运行模式
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间
    meta = {
        'collection':'devices_setup_configure'
    }

#设备状态记录
class DevicesStatusLog(db.Document):
    device = db.ReferenceField(Devices)#设备
    status = db.IntField()#设备状态,例如开关机等.
    error = db.IntField()#设备故障

    remind= db.BooleanField()#更换滤网提醒

    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间
    meta = {
        'collection':'devices_status_log'

    }

#设备数据记录
class DevicesDataLog(db.Document):
    device = db.ReferenceField(Devices)#设备
    temperature = db.IntField()#温度
    moisture = db.IntField()#湿度
    co2 = db.IntField()#C02
    pm25 = db.IntField()#PM2.5
    formalde = db.IntField()#甲醛
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间
    meta = {
        'collection':'devices_data_log'

    }

#配送地址
class Addresses(db.Document):
    user = db.ReferenceField(Users)#用户
    desc = db.StringField()#地址描述,格式:省-市-县 / 街道 / 联系电话
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间
    meta = {
        'collection':'addresses'

    }

#设备配件
class Parts(db.Document):
    # device = db.ReferenceField(Devices)
    id = db.StringField(unique=True, required=True)# 对应的产品id
    pid = db.StringField(unique=True, required=True)#配件编码
    name = db.StringField()#配件名称
    desc = db.StringField()#配件描述
    price = db.FloatField()#配件价格
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间
    meta = {
        'collection':'parts'

    }

#订单
class Orders(db.Document):
    oid = db.StringField(unique=True, required=True)#订单编码
    user = db.ReferenceField(Users)#用户
    device = db.ReferenceField(Devices)
    part = db.ReferenceField(Parts)#配件
    address = db.ReferenceField(Addresses)#地址
    desc = db.StringField()#订单描述
    quantity = db.IntField()#数量
    amount = db.FloatField()#总金额

    sendWay = db.StringField()#配送方式
    message = db.StringField()#留言内容

    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#创建时间
    meta = {
        'collection':'orders'

    }

#订单状态记录
class OrdersStatusLog(db.Document):
    order = db.ReferenceField(Orders)
    tid = db.StringField(unique=True, required=True)#支付编码
    status = db.IntField()#状态描述
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#创建时间
    meta = {
        'collection':'orders_status_log'

    }

#设备绑定记录
class DevicesBoundLog(db.Document):
    user = db.ReferenceField(Users)#用户
    device = db.ReferenceField(Devices)#设备
    is_active = db.BooleanField(default=True)#记录有效性
    created_time = db.DateTimeField(default=datetime.datetime.now)#记录时间
    meta = {
        'collection':'devices_bound_log'
    }
