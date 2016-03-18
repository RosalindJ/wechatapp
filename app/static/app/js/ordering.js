(function($){
	$(document).on("ready",function(){
		// 点击返回上一级
		$(".backBtn").eq(0).on("click",function(){
			window.history.back();
		});
		// 当街道的长度太过，显示不全时，将它的长度变为100%
		//if($("#hideStreet").width()>$("#street").width()){
		//	$("#street").width("100%");
		//}
		// 当鼠标焦点在文本输入时，将展开全部
		$("#message").on("focus",function(){
			$("#messBox").height("inherit");
		});
		// 当失去焦点，文本框没有输入内容时，收起
		$("#message").on("blur",function(){
			if(!$(this).val()){
				$("#messBox").height("1rem");
			}				
		});


		//这里要修改,根据微信支付来进行修改
		// 控制多次提交订单
		var control = true;
		$(".payBnt").eq(0).on("click",function(){
			if(control){
				//判断合计金额是否大于0
				if(Number($("#amount").html()) > 0 && $("#name").val() && $("#tel").val() && $("#street").val()){
					// 发出ajax请求，将数据传递给服务器
					$.ajax({
						type:"POST",
						url:"/orderingDetail",
						// 产品编号,数量，合计价格，收货人，地址，电话,留言
						data:"netId="+$("#pro_name").attr("data-netid")+"&price="+$("#price").html()+"&quantity="+$("#num").val()+"&sendWay="+$("#sendWay").html()+"&name="+$("#name").val()+"&tel="+$("#tel").val()+"&address="+$("#street").val()+"&message="+$("#message").val()+"&amount="+$("#amount").html(),
						success:function(data){
							if(data == 'yes'){
								console.log("success");
								alert("亲,成功付款");
								control = false;
							}
						},
						error:function(){
							console.log("error");
						}
					})
				}else{
					alert("亲,订单没完整填写");
				}

			}else{
				console.log("已经下单成功");
				alert("亲,成功付款");
			}		
		})
	
		// 调用SUI Moblie 的省市区选择器
		//$("#city-picker").cityPicker({
		//	toolbarTemplate: '<header class="bar bar-nav">\
		//	<button class="button button-link pull-right close-picker">确定</button>\
		//	<h1 class="title">选择收货地址</h1>\
		//	</header>'
		//});
		// 增加数量
		$.fn.addNum = function(e_1,e_2,e_3,e_4,spacing,max){
			$(e_1).on("click",function(){
				var tem = Number($(e_2).val())+spacing;
				$(e_2).val(tem);
				$(e_4).html(Number($(e_3).html())*tem);
			})
		}
		// 减少数量
		$.fn.reduceNum = function(e_1,e_2,e_3,e_4,spacing,min){
			$(e_1).on("click",function(){
				var tem = Number($(e_2).val())-spacing;
				if(tem < min){
					tem = 0;
				}
				$(e_2).val(tem);	
				$(e_4).html(Number($(e_3).html())*tem);			
			})
		}
		$.fn.addNum("#add","#num","#price","#amount",1);
		$.fn.reduceNum("#reduce","#num","#price","#amount",1,0);
	})	
}(Zepto));
	  