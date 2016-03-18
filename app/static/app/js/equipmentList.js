/**
 * Created by tangmeirong on 16/3/17.
 */
    $(".codeBnt").click(function(event) {
        console.log("点击了")
        wx.ready(function () {
            /*调起微信扫一扫接口*/
            wx.scanQRCode({
                needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
                scanType: ["qrCode", "barCode"], // 可以指定扫二维码还是一维码，默认二者都有
                success: function (res) {
                    var result = res.resultStr; // 当needResult 为 1 时，扫码返回的结果
                    //这里还需要对扫描结果进行判断,符合了才发送ajax,目前还不知道产品二维码的结果格式什么的,所以还没做判断
                    var reg = /^[0-9]{11}$/g;
                    if (reg.test(result)) {
                        $.ajax({
                            type: "POST",
                            url: "/testing_app1/equipmentIndex",
                            data: "codeResult=" + result,
                            //data:"codeResult=12345",
                            success: function (data) {
                                console.log(data);
                                if(data == 'yes'){
                                    window.location.href = "addEquipment";
                                }else{
                                    //数据没有成功接收
                                    $(".page").eq(2).addClass("page-current").siblings().removeClass("page-current");
                                }
                            },
                            error: function () {
                                //ajax发送不成功
                                 $(".page").eq(2).addClass("page-current").siblings().removeClass("page-current");
                                console.log("error");
                            },
                        })
                    } else {
                        //    这里是扫描产品不符合的处理
                        $(".page").eq(2).addClass("page-current").siblings().removeClass("page-current");

                    }

                },
                error: function () {
                    //    这里是调用扫一扫失败的处理
                    $(".page").eq(2).addClass("page-current").siblings().removeClass("page-current");
                }
            });
        })

        wx.error(function (res) {
            alert(res.errMsg);
            //config信息验证失败会执行error函数，如签名过期导致验证失败，具体错误信息可以打开config的debug模式查看，也可以在返回的res参数中查看，对于SPA可以在这里更新签名。
        });
    });

    // wifi 添加设备
    $(".wifiBnt").click(function(event) {
        console.log("yes")
        // 调用手机wifi
        // 出现搜索同wifi 下的设备页面
        $(".page").eq(1).addClass("page-current").siblings().removeClass("page-current");
        //如果wifi成功的话
        //window.location.href = "addaddEquipment";

	});


    var allHeight = document.documentElement.clientHeight;
    // WiFi搜索中为视口的高度
    $("#wifi_ing").height(allHeight);
