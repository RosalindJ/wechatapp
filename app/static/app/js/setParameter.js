(function($){
	$(document).on("ready",function(){
		// 点击返回
		$(".backBtn").eq(0).on("click",function(){
			window.history.back();
		})

		var barHeight = $(".bar-nav ~ .content").offset().top;
		var tem = $(window).height() - barHeight;
		$(".wrap").eq(0).height(tem);

		// 点击保存按钮触发ajax，向服务器发送数据
		$(".saveBtn").eq(0).on("click",function(){
			// ajax
			$.ajax({
				type:"POST",
				url:"/testing_app1/setParameter",
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