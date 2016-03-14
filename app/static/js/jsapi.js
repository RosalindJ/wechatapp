/**
 * Created by tangmeirong on 16/3/11.
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
  wx.ready(function () {
  /*调起微信扫一扫接口*/
        wx.scanQRCode({
             needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
             scanType: ["qrCode", "barCode"], // 可以指定扫二维码还是一维码，默认二者都有
             success: function (res) {
                var result = res.resultStr; // 当needResult 为 1 时，扫码返回的结果
             }
        });
  })

  wx.error(function (res) {
      alert(res.errMsg);
  });


    var Btn = document.getElementsByClassName("Btn")[0];
    Btn.onclick = function(){
        console.log("点击了")
    }