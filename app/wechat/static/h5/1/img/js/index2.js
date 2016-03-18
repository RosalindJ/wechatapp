$(window).ready(function(){	
	$(".page8_bg").click(function(){
		$(".block").hide();
	})
	$(".page8_bg2").click(function(){
		$(".block").hide();
	})
	var flagUser = false,flagNum = false;
	var regName = /^[\u4e00-\u9fa5]*$/;
	var regTel = /^[1][358][0-9]{9}$/;
	//var regTel = /((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)/;
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