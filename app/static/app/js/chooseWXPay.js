/**
 * Created by tangmeirong on 16/3/21.
 */
 /*
 * 注意：
 * 1. 所有的JS接口只能在公众号绑定的域名下调用，公众号开发者需要先登录微信公众平台进入“公众号设置”的“功能设置”里填写“JS接口安全域名”。
 * 2. 如果发现在 Android 不能分享自定义内容，请到官网下载最新的包覆盖安装，Android 自定义分享接口需升级至 6.0.2.58 版本及以上。
 * 3. 完整 JS-SDK 文档地址：http://mp.weixin.qq.com/wiki/7/aaa137b55fb2e0456bf8dd9148dd613f.html
 *
 * 如有问题请通过以下渠道反馈：
 * 邮箱地址：weixin-open@qq.com
 * 邮件主题：【微信JS-SDK反馈】具体问题
 * 邮件内容说明：用简明的语言描述问题所在，并交代清楚遇到该问题的场景，可附上截屏图片，微信团队会尽快处理你的反馈。
 */
function wxPay(data){
    wx.ready(function () {
        /*调起微信扫一扫接口*/
        wx.chooseWXPay({
            timestamp: data["timeStamp"], // 支付签名时间戳，注意微信jssdk中的所有使用timestamp字段均为小写。但最新版的支付后台生成签名使用的timeStamp字段名需大写其中的S字符
            nonceStr:''+data["nonceStr"]+'', // 支付签名随机串，不长于 32 位
            package: ''+data["package"]+'', // 统一支付接口返回的prepay_id参数值，提交格式如：prepay_id=***）
            signType: ''+data["signType"]+'', // 签名方式，默认为'SHA1'，使用新版支付需传入'MD5'
            paySign: ''+data["paySign"]+'', // 支付签名
            success: function (res) {
            // 支付成功后的回调函数
            alert(res.errMsg);
            },
            cancel:function(res) {
                alert(res);
            }
    });
    })

    wx.error(function (res) {
        alert(res.errMsg);
        //config信息验证失败会执行error函数，如签名过期导致验证失败，具体错误信息可以打开config的debug模式查看，也可以在返回的res参数中查看，对于SPA可以在这里更新签名。
    });
}

