from .pay import JsApi_pub,UnifiedOrder_pub
from .config import WxPayConf_pub
import time

class jsApiParameters(object):
    def getJsParameters(self):

        # 第一步网页授权获取用户openid
        code = None;
        JsApi_pub.setCode(code)
        openid = JsApi_pub.getOpenid();

        # 第二步:使用统一支付接口,获取prepay_id
        # 设置必填参数
        # 用户标识
        UnifiedOrder_pub.setParameter("openid",openid)
        # 商品描述
        UnifiedOrder_pub.setParameter("body","贡献一分钱")
        # 订单号自定义,此处举例
        timeStamp = int(time.time())
        out_trade_no = WxPayConf_pub["APPID"]+timeStamp
        UnifiedOrder_pub.setParameter("out_trade_no",out_trade_no)
        # 总金额
        UnifiedOrder_pub.setParameter("total_fee","1")
        # 收货地址,这里的NOTIFY——URL根据需要是否使用共享收货地址而定
        UnifiedOrder_pub.setParameter("notify_url",WxPayConf_pub["NOTIFY_URL"])
        # 交易类型
        UnifiedOrder_pub.setParameter("trade_type","JSAPI")

        prepay_id = UnifiedOrder_pub.getPrepayId()

        # 第三步使用JsApi_pub调起支付
        JsApi_pub.setPrepayId(prepay_id)
        jsApiParameters = JsApi_pub.getParameters()

        return jsApiParameters