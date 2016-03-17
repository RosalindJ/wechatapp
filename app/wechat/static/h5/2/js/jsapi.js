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
  var shareData = {
    title: '我的第一次要在丽江，你约吗？',
    desc: '2016年1月30日在丽江花园-渔人码头广场举行兆晶智能舒适新风机内购会，敬请参加！',
    link: 'http://mp.weixin.qq.com/s?__biz=MzI1OTA3Njg5Ng==&mid=447484877&idx=1&sn=1e123f9ee2c5bd654a55d6ca10ad2ae7#rd',
    imgUrl: 'https://mmbiz.qlogo.cn/mmbiz/ClNzL9Zp0OOYCGLjSUB3vSNR71HW3ibibawloRI6uQlcqgsepNEtK4vliac3GxdRVQ1zub0SEl3ibPic9Hx0Lyicddbg/0?wx_fmt=jpeg'
  };
  wx.onMenuShareAppMessage(shareData);
  wx.onMenuShareTimeline(shareData);

  function decryptCode(code, callback) {
    $.getJSON('/jssdk/decrypt_code.php?code=' + encodeURI(code), function (res) {
      if (res.errcode == 0) {
        codes.push(res.code);
      }
    });
  }
});

wx.error(function (res) {
  alert(res.errMsg);
});

