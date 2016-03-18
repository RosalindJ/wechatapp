(function($){
	// 发送请求ajax,接受服务器数据
	//$.ajax({
	//	type:"POST",
	//	url:"/order",
	//	success:function(data){
	//		console.log(data + "1");
	//		// 有中文转化为中文编码，代替Unicode
	//		data = unescape(data.replace(/\\u/g, "%u"));
	//		console.log(data + "2");
	//		if(data != ""){
	//			var json_data = JSON.parse(data);
	//			$(".page").eq(1).addClass("page-current").siblings('.page').removeClass("page-current");
	//			for(var i = 0,len = json_data.length;i < len; i++){
	//			autoOrder(json_data[i].orderNum,json_data[i].tradingStatus,json_data[i].netImgUrl,json_data[i].netName,json_data[i].adapterodel,json_data[i].quantity,json_data[i].sumMoney);
    //
	//			}
	//			console.log(json_data.length);
	//		}else{
	//			$(".page").eq(0).addClass("page-current").siblings('.page').removeClass("page-current");
	//		}
	//	},
	//	error:function(){
	//		console.log("error");
	//	}
	//})

	//自动生成订单列表 
	//function autoOrder(data_1,data_2,data_3,data_4,data_5,data_6,data_7){
	//	$.init();
	//	// 加载flag
	//	var loading = false;
	//	// 最多可加载的条目,后期修改为数据库总条数
	//	var maxItems = 26;
    //
	//	// 每次加载添加多少条目
	//	var itemsPerLoad = 1;
    //
	//	function addItems(number, lastIndex) {
	//	    // 生成新条目的HTML
	//	    var html = '';
	//	    var len = lastIndex + number;
	//	    // 控制生成条数不能大于最多加载的总条数
	//	    if(len >= maxItems){
	//	    	len = maxItems;
	//	    }
	//	    for (var i = lastIndex + 1; i <= len; i++) {
	//	        html += '<li class="card"><div class="header clearfix"><!-- 订单号 --><span class="codeBox">订单号：<span class="code">'+data_1+'</span></span><!-- 交易状态 --><span class="statusBox">交易状态：<span class="status">'+ data_2 +'</span></span></div><div class="card-content"><div class="card-content-inner row"><!-- 滤网图片 -->'+
	//	        '<img src="' + data_3 + '" class="netImg col-33"><div><!-- 滤网名称 --><h2>' + data_4 + '</h2><!-- 滤网说明 --><span class="config">适配机型：' + data_5 + '</span><p class="clearfix"><!-- 购买数量 --><span class="quantityBox">数量： <span class="quantity">' + data_6 + '</span></span><!-- 购买合计金额 --><span class="amountBox">合计：<span class="amount">' + data_7 + '元</span></span></p></div></div></div></li>';
	//	    }
	//	    // 添加新条目
	//	    $('.infinite-scroll-bottom .list-container').append(html);
	//	}
	//	//预先加载几条
	//	addItems(itemsPerLoad, $('.list-container li').length);
    //
	//	// 上次加载的序号
	//	var lastIndex = $('.list-container li').length;
    //
	//	// 注册'infinite'事件处理函数
	//	$(document).on('infinite', '.infinite-scroll-bottom',function() {
    //
	//	    // 如果正在加载，则退出
	//	    if (loading) return;
    //
	//	    // 设置flag
	//	    loading = true;
    //
	//	    // 模拟1s的加载过程
	//	    setTimeout(function() {
	//	        // 重置加载flag
	//	        loading = false;
    //
	//	        if (lastIndex >= maxItems) {
	//	            // 加载完毕，则注销无限加载事件，以防不必要的加载
	//	            $.detachInfiniteScroll($('.infinite-scroll'));
	//	            // 删除加载提示符
	//	            $('.infinite-scroll-preloader').remove();
	//	            return;
	//	        }
	//	        // 添加新条目
	//	        addItems(itemsPerLoad, lastIndex);
	//	        // 更新最后加载的序号
	//	        lastIndex = $('.list-container li').length;
	//	        //容器发生改变,如果是js滚动，需要刷新滚动
	//	        $.refreshScroller();
	//	    }, 1000);
	//	});
	//}
	
	// 使用事件委托
	$(".list-container").on("click","li",function(e){
		// console.log(e.currentTarget.children[0].children[0].children[0].innerText);
		// 将点击的订单号暂存放到临时存储中，为跳转订单详情做准备
		sessionStorage.orderCode = e.currentTarget.children[0].children[0].children[0].innerText;
		// 还要实现跳转订单详情页面
		window.location.href = "orderdetail";
	})
})(Zepto)