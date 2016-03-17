(function($){
	$(document).on("ready",function(){
	
		// 获得温度湿度co2的数据
		var json_data;
		$.ajax({
			type:"POST",
			url:"/getParameter",
			success:function(data){
				console.log(data);
				if(data){
					json_data = JSON.parse(data);
					$("#temperature").val(json_data.temper.temfit);
					$("#carbon").val(json_data.co2.co2fit)
					$("#moisture").val(json_data.damp.dampfit);

					// 调用四个方法

					$.fn.addNum(".add",".fill",0,1,json_data.temper.temMax);
					$.fn.addNum(".add",".fill",1,1,json_data.damp.dampMax);
					$.fn.addNum(".add",".fill",2,1,json_data.co2.co2Max);

					$.fn.reduceNum(".reduce",".fill",0,1,json_data.temper.temMin);
					$.fn.reduceNum(".reduce",".fill",1,1,json_data.damp.dampMin);
					$.fn.reduceNum(".reduce",".fill",2,1,json_data.co2.co2Min);

					$.fn.inputNumber(".fill",0);
					$.fn.inputNumber(".fill",1);
					$.fn.inputNumber(".fill",2);

					$.fn.controlNumber(".fill",0,json_data.temper.temMax,json_data.temper.temMin);
					$.fn.controlNumber(".fill",1,json_data.damp.dampMax,json_data.damp.dampMin);
					$.fn.controlNumber(".fill",2,json_data.co2.co2Max,json_data.co2.co2Min);
				}
			},
			error:function(){
				console.log("error");
			}
		})
		// 点击返回
		$(".backBtn").eq(0).on("click",function(){
			window.history.back();
		})	

		var barHeight = $(".bar-nav ~ .content").offset().top;
		var tem = $(window).height() - barHeight;
		$(".wrap").eq(0).height(tem);

		// 初始化输入框
		// $.fn.initInput = function(e_1,index,value){
		// 	$(e_1).eq(index).val(value);
		// }
		// 增加数值
		$.fn.addNum = function(e_1,e_2,index,spacing,max){
			$(e_1).eq(index).on("click",function(){
				var temp = Number($(e_2).eq(index).val())+spacing;						
					if(temp > max){
						temp = max;
					}						
				$(e_2).eq(index).val(temp);
			})
		}

		//减少数值
		$.fn.reduceNum = function(e_1,e_2,index,spacing,min){
			$(e_1).eq(index).on("click",function(){
				var temp = Number($(e_2).eq(index).val())-spacing;							
					if(temp < min){
						temp = min;
					}					
				$(e_2).eq(index).val(temp);
			})
		}

		// 判断输入的只能是数字
		$.fn.inputNumber = function(e_1,index){
			var reg = /^[0-9]*$/;
			$(e_1).eq(index).on("input",function(){
				if(!reg.test($(this).val())){
					var len = $(this).val().length-1;
					while(!reg.test($(this).val().slice(0,len))){
							len--;
					}
					if(len <= 0){
						$(this).val("");
					}else {
						$(this).val($(this).val().slice(0,len));
					}
				}
			})
		};

		// 控制输入的值，不能小于最小值，不能大于最大值
		$.fn.controlNumber = function(e_1,index,max,min){
			$(e_1).eq(index).on("blur",function(){
				if($(this).val() < min){
					$(this).val(min);
				}else if($(this).val() > max){
					$(this).val(max);
				}
			});
		}

		// 调用上述四个方法
		// var array = [{aMax:30,rMin:16,spacing:1},{aMax:100,rMin:20,spacing:1},{aMax:100,rMin:20,spacing:1}];
		// for(var i = 0; i < $(".add").length;i++){
			// $.fn.initInput(".fill",i,array[i]["rMin"]);
		// 	$.fn.addNum(".add",".fill",i,array[i]["spacing"],array[i]["aMax"]);
		// 	$.fn.reduceNum(".reduce",".fill",i,array[i]["spacing"],array[i]["rMin"]);
		// 	$.fn.inputNumber(".fill",i);
		// 	$.fn.controlNumber(".fill",i,array[i]["aMax"],array[i]["rMin"]);
		// }

		// 点击保存按钮触发ajax，向服务器发送数据
		$(".saveBtn").eq(0).on("click",function(){
			// ajax
			$.ajax({
				type:"POST",
				url:"/setParameter",
				data:"temfit=" + $("#temperature").val()+"&dampfit=" + $("#moisture").val() + "&co2fit=" + $("#carbon").val(),
				success:function(){
					console.log("success");
				},
				error:function(){
					console.log("error");
				}
			})
		})
	})			
			
})(Zepto)