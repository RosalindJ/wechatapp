(function($){
		// 点击返回上一级
		$(".backBtn").eq(0).on("click",function(){
			window.history.back();
		});
		// 点击添加设定时间
		for(var i = 0;i < $(".addTimeBnt").length;i++){
			(function(i){
				$(".addTimeBnt").eq(i).on("click",function(){
					if(i == 0){
						// 点击开机设定按钮，暂存timeType为open
						sessionStorage.timeType = "open";
					}else{
						// 点击关机设定按钮，暂存timeType为close
						sessionStorage.timeType = "close";
					}
					window.location.href = "setingTime";
				})
			})(i);
		}

		// ajax,向服务器请求设定开关机时间的数据
		function AcceptAjax(URL,parent){
			$.ajax({
				type:"POST",
				url:URL,
				success:function(data){
					console.log("success"+ data + "ddd");
					if(data){
						// 里面的data，要看后台那边传送过来的数据格式,checkbox ,根据服务器返回的值，已经开启的话，添加 data-select="true"，否则添加data-select="false"
						$('<li><!-- 设定的时间 --><div class="item-title-row row no-gutter "><div class="item-title col-80"><span class="time">data</span><div class="prompt"><p><span class="hour">data</span>小时<span class="minute">data</span>分钟</p><span class="count">data</span></div></div><div class="item-after col-20"><!-- 关闭——开启按钮 --><div class="item-input"><label class="label-switch"><input type="checkbox" id="databox"><div class="checkbox" id="data" data-select="false"></div></label></div></div></div></li>').prependTo(parent);

						// 这里是控制已经select的，就控制相应的checked为true
						// if($("#data").attr("data-select") == "true"){
						// 	$("#databox").get(0).checked = true;
						// }
					}
				},
				error:function(){
					console.log("error");
				}
			})
		}
		// 接受开机设定的数据
		AcceptAjax("/openTimeList","#openTimeList");
		// 接受关机设定的数据
		AcceptAjax("/closeTimeList","#closeTimeList");

		// 发送请求数据给服务器
		function sendAjax(URL,id,data_select){
			$.ajax({
				type:"POST",
				url:URL,
				// timeId,应该放到html内，然后设置display：none
				data:"timeId=" + id+"&selected=" + data_select,
				success:function(){
					console.log("success");
				},
				error:function(){
					console.log("error");
				}
			})
		}

		function isSelect(element){
			$(element).on("click",".checkbox",function(e){
				console.log(e)
				// checkbox的id存放的是时间的timeId,data-select存放的为是否开启
				if(e.target.attributes["data-select"]["nodeValue"] == "true"){
					e.target.attributes["data-select"]["nodeValue"] = "false";
				}else{
					e.target.attributes["data-select"]["nodeValue"] = "true";
				}
				sendAjax("",e.target.attributes["id"]["nodeValue"],e.target.attributes["data-select"]["nodeValue"]);
			});
		}
		// 开机，点击checkbox，发一次ajax请求
		isSelect("#openTimeList");		

		// 关机，点击checkbox，发一次ajax请求
		isSelect("#closeTimeList");

	})(Zepto)