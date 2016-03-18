$(window).ready(function(){
	// 图片的预加载
	var imgArr = [];
	var imgNum = 0;
	for(var i = 0,len = $("#wrap img").length;i < len;i++){
		imgArr[i] = new Image();
		imgArr[i].onload = function(){
			imgNum++;
			if(imgNum == len) {
				$(".page1").show();
				$(".music").get(0).play();
			}
		}
		imgArr[i].src = $("img").eq(i).attr("src");
	}

	// page8	
	$(".page8_bg").click(function(){
		$(".block").hide();
	})
	$(".page8_bg2").click(function(){
		$(".block").hide();
	})
	// 验证
	// 姓名的验证 输入中文
	var flagUser = false,flagNum = false;
	var regName = /^[\u4e00-\u9fa5]*$/gm;
	// 电话号码的验证 手机号 3-4位区号，7-8位直播号码，1－4位分机号
	var regTel = /((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)/;
	$(".username").on("input",function(){
		if(($(".username").val() == "") || (!regName.test($(".username").val()))){
			$(".icon2").show();
			$(".icon1").hide();
		}else{
			$(".icon1").show();
			$(".icon2").hide();
			flagUser = true;
		}
	});
	$(".telNum").on("input",function(){
		if(($(".telNum").val() == "") || (!regTel.test($(".telNum").val()))){
			$(".tel_icon2").show();
			$(".tel_icon1").hide();
		}else{
			$(".tel_icon1").show();
			$(".tel_icon2").hide();
			flagNum = true;
		}
	});
	var yuyueflag = true;
	$(".yudingBtn").click(function(){
		if(flagUser == true && flagNum == true && yuyueflag == true){		
			$.ajax({
				type:"POST",
				url:"/presell",
				data:"username="+ $(".username").val()+"&phone="+$(".telNum").val(),
				success:function(data){
					console.log(data)
					if(data == "yes"){
						yuyueflag = false;
						$(".block").show();
					}
				}
			})
		}
	});
})