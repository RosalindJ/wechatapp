(function($){
		// 点击返回上一级
		$(".backBtn").eq(0).on("click",function(){
			// window.history.back();
			window.location.href = "/testing_app1/setup";
		});
		// 时间设定的开关
		for(var i = 0,len = $(".data").length; i < len;i++){
			if ($(".data").eq(i).attr("data-select") == "true") {
				$(".data").eq(i).siblings('input').prop('checked',"true");
				console.log("checked");
			}else{
				$(".data").eq(i).siblings('input').prop('checked',"");
				console.log("no-checked");
			}
		}

		// 点击添加设定时间
		for(var i = 0;i < $(".addTimeBnt").length;i++){
			(function(i){
				$(".addTimeBnt").eq(i).on("click",function(){
					if(i == 0){
						// 点击开机设定按钮，暂存timeType为openTime
						sessionStorage.timeType = "openTime";
					}else{
						// 点击关机设定按钮，暂存timeType为closeTime
						sessionStorage.timeType = "closeTime";
					}
					window.location.href = "/testing_app1/setingTime";
				})
			})(i);
		}

		// 发送请求数据给服务器
		function sendAjax(URL,id,data_select){
			$.ajax({
				type:"POST",
				url:URL,
				// timeId,应该放到html内，然后设置display：none
				data:"timeId=" + id +"&Tselect=" + data_select,
				success:function(){
					console.log("success");
				},
				error:function(){
					console.log("error");
				}
			})
		}

		//点击开关 设置data-selcet,data-selcet和开关绑定在一起
		function isSelect(element){
			$(element).on("click",function(){
				if($(this).attr("data-select") == "true"){

					$(this).attr("data-select",false);
				}else{
					$(this).attr("data-select",true);
					console.log("checked");
				}
				// console.log($(this).parents("ul").attr("id"))
				sendAjax("/testing_app1/setTime",$(this).parents("ul").attr("id"),$(this).attr("data-select"));
			})
		}

		// 点击checkbox，发一次ajax请求
		isSelect(".data");
	})(Zepto)