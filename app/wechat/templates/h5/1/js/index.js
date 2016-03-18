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

	// page1
	$(".page1 .con9").get(0).addEventListener("webkitAnimationEnd",function(){
		$(".page1 .mask").removeClass("showmask");
		$(".con_bg").show();
		$(".con1").show();
	},false);
	$(".click").click(function(){
		$(this).hide();
		$(".con_bg").removeClass("bounceInDown").animate({
			"opacity":"0"
		},500);
		$(".con1").removeClass("slideInRightP").addClass("slideOutLeft");
		setTimeout(function(){
			$(".page1 .person2").hide();
			$(".page1 .person1").show().addClass("animated runleft");
			$(".page1").addClass("animated scaleDoor");
			setTimeout(function(){
				$(".page1").hide();
				$(".page2").show();
			},1000);
		},500);
	})

	// page2
	$(".click2").click(function(){
		$(this).hide();
		// 门开
		$(".door2").addClass("dooropen");
		// 人走进卧室
		$(".person_p2").addClass("perrun");
		$(".person_p2").get(0).addEventListener("webkitAnimationEnd",function(){
			$(".door2").removeClass("dooropen").addClass("doorclose");
			$(".p2_windl").css("zIndex",10);
			// 字体出现
			setTimeout(function(){
				$(".con_bg_p2").show();
				$(".con2").show();
				setTimeout(function(){
					// 风关闭 设备关闭
					$(".p2_windl").fadeOut();
					// 字离开
					setTimeout(function(){
						$(".con_bg_p2").removeClass("bounceInDown").animate({
							"opacity":"0"
						},500);
						$(".con2").removeClass("slideInRightP").addClass("slideOutLeft");
						// 出现第三页面
						setTimeout(function(){
							$(".page2").hide();
							$(".page3").show();
							page3();
						},1500);
					},1000);
				},2000);
			},1000);
		},false);
	})

	// page3
	function page3(){
		// 走到床边的动画完成时 上床睡觉
		$(".person_p3").get(0).addEventListener("webkitAnimationEnd",function(){
			$(".person_p3").hide();
			$(".page3 .bed").fadeOut();
			$(".page3 .bed2").fadeIn();	
			$(".con_bg_p3").show();
			$(".con6").show();
		},false);
		// 检测器动画完成时 出现风
		$(".page3 .circle4").get(0).addEventListener("webkitAnimationEnd",function(){			
			// 设备开启
			$(".p3_windl").show();
			$(".p3_windt").show();
			// 卧室变暗  关灯睡觉
			setTimeout(function(){
				$(".page3 .mask").fadeIn();
				// 卧室变亮 早晨起床
				setTimeout(function(){
					$(".con_bg_p3").removeClass("bounceInDown").animate({
						"opacity":"0"
					},500);
					$(".con6").removeClass("slideInRightP").addClass("slideOutLeft");
					setTimeout(function(){
						$(".page3 .mask").fadeOut();
						// 早上起床的对话框
						setTimeout(function(){
							$(".con_bg_p3").hide();
							$(".con7").show().addClass("animated tada");
							// 人走出卧室
							setTimeout(function(){
								$(".con7").fadeOut();
								setTimeout(function(){
									$(".page3 .bed2").hide();
									$(".page3 .bed").show();
									$(".person1_p3").show().addClass("animated outbed");
									$(".person1_p3").get(0).addEventListener("webkitAnimationEnd",function(){
										setTimeout(function(){
											$(".page3").hide();
											$(".page4").show();
											page4();
										},500);
									},false);
								},1500);
							},2000);
						},1000);
					},2000);
				},1000)	
			},1000);
		},false);
	}
	// page3();

	var eatArr = [".game1",".game2",".game3",".mouth"]
	// 拖动的开始和移动的函数
	var flagmove = true;
	var dragNum = 0;
	function dragMove(element1,element2){
		var mouseX,mouseY;
		var $element1 = $(element1).get(0);
		var $page4 = $(".page4").get(0);
		var $element2 = $(element2).get(0);
		$element1.addEventListener("touchstart",function(event){
			var event = event || window.event;
			mouseX = event.touches[0].clientX - $element1.offsetLeft;
			mouseY = event.touches[0].clientY - $element1.offsetTop;
			event.preventDefault();//uc、qq浏览器的Bug,加上这个就可，但也可能会导致其他的bug出现
		},false);
		$element1.addEventListener("touchmove",function(event){
			var event = event || window.event;
			var nLeft = event.touches[0].clientX - mouseX;
			var nTop =  event.touches[0].clientY - mouseY;
			if(nLeft<0){
				nLeft = 0;
			}else if(nLeft>$page4.offsetWidth - $element1.offsetWidth){
				nLeft = $page4.offsetWidth - $element1.offsetWidth;
			}
			if(nTop<0){
				nTop = 0;
			}else if(nTop>$page4.offsetHeight - $element1.offsetHeight){
				nTop = $page4.offsetHeight - $element1.offsetHeight;
			}
			$element1.style.top = nTop + "px";     
			$element1.style.left = nLeft + "px";
		},false);
	}	
	function drag1(element1,element2){
		var mouseX,mouseY;
		var $element1 = $(element1).get(0);
		var $element2 = $(element2).get(0);
		var $page4 = $(".page4").get(0);
		dragMove(element1,element2);

		$element1.addEventListener("touchend",function(event){
			var event = event || window.event;
			if(($(element1).position().top + $(element1).height() < $(element2).position().top + $(element2).height())
			&& ($(element1).position().top > $(element2).position().top)
			&& ($(element1).position().left + $(element1).width() < $(element2).position().left + $(element2).width())
			&& ($(element1).position().left > $(element2).position().left)){		
				$(".p4_phone").show();
				$(".con8").fadeOut();
				p4_phone();
				$(".click3").show();
				$(".game1").fadeOut();
				$(".game2").fadeOut();
				$(".game3").fadeOut();
				$(".mouth").fadeOut();
			}
		},false);
	}
	function p4_phone(){
		var time5 = null;
		var beginNum = 200;
		var maxT = 500;
		time5 = setInterval(function(){
			beginNum+=5;
			if(beginNum<=maxT){
				$(".page4 .p4_pmvalue").html(beginNum);
			}else{
				clearInterval(time5);
				$(".p4_loading").removeClass("loadingrotate");
				setTimeout(function(){
					$(".p4_loading").fadeOut();
					$(".p4_jianceing").fadeOut();
					$(".p4_wuran").fadeIn(1000);
					$(".p4_jiance2").fadeIn(1000);
					$(".p4_sugg1").addClass("fadeInword");
					$(".p4_btn").click(function(){
						$(".p4_tips").show().addClass("fadeInOut_p4");
					    $(".p4_tips").get(0).addEventListener("webkitAnimationEnd",function(){
							$(".p4_phone").addClass("slideOutRightP");
							setTimeout(function(){
								$(".page4 .mask").fadeOut();
								$(".p4_windl").css("opacity","1");
				                $(".p4_windt").css("opacity","1");
				                $(".con_bg_p4").show();
				                $(".con4").fadeIn();
							},2100);
						},false);
					});
				},1000);
			}
		},40)
	}
	// page4
	function page4(){
		drag1(eatArr[0],eatArr[3]);
		drag1(eatArr[1],eatArr[3]);
		drag1(eatArr[2],eatArr[3]);
		// 点击屏幕时 人移动，出门
		$(".click3").click(function(){
			$(".p4_phone").remove();
			$(this).hide();
			$(".con_bg_p4").animate({
				"opacity":"0"
			},500);
			$(".con4").addClass("slideOutLeft");
		    $(".con4").get(0).addEventListener("webkitAnimationEnd",function(){
		   		$(".con4").hide();
		    },false);
			$(".p4_person2").hide();
			$(".p4_person1").show().addClass("animated rundoor");
			setTimeout(function(){
				$(".living_room2").addClass("scalespeed1");
				$(".p4_person1").addClass("scalespeed2");
				setTimeout(function(){
					$(".page5").show();
					$(".page4").hide();
					setTimeout(function(){
						page5();
					},1000);
				},1100);
			},60);
		});
	}
	// page4();
	// page5
	function page5(){
		$(".door3").addClass("dooropen2");
		$(".p5_person1").addClass("perrun2");
		$(".p5_person1").get(0).addEventListener("webkitAnimationEnd",function(){
			$(".door3").removeClass("dooropen2").addClass("doorclose");
			$(".p5_windl").css("zIndex",10);
			// 字体出现
			setTimeout(function(){
				$(".con_bg_p5").show();
				$(".con2_p5").show();
				setTimeout(function(){
					// 风关闭 设备关闭
					$(".p5_windl").fadeOut();
					// 字离开
					setTimeout(function(){
						$(".con_bg_p5").removeClass("bounceInDown").animate({
							"opacity":"0"
						},500);
						$(".con2_p5").removeClass("slideInRightP").addClass("slideOutLeft");
						// 出现第5页面
						setTimeout(function(){
							$(".page5").hide();
							$(".page6").show();
							page6();
						},1500);
					},1000);
				},2000);
			},1000);
		},false);
	}
	// page5();
    // page6
	function page6(){
		$(".clockhour").addClass("clockrotateH");
		setTimeout(function(){
			// 回家前的一小时
			$(".page6 .con_bg_p6").show();
			$(".page6 .con5").show();
			setTimeout(function(){
				$(".page6 .con5").removeClass("slideInRightP").addClass("slideOutLeft");
				$(".page6 .con_bg_p6").fadeOut();
				setTimeout(function(){
					// 检测器检测到无人
					$(".page6 .p6_circle1").show().addClass("showcircle1");
					$(".page6 .p6_circle2").show().addClass("showcircle1 showcircle2");
					$(".page6 .p6_circle3").show().addClass("showcircle1 showcircle3");
					$(".page6 .p6_circle4").show().addClass("showcircle1 showcircle4");
					$(".page6 .p6_circle5").show().addClass("showcircle1 showcircle5");
					$(".page6 .p6_circle6").show().addClass("showcircle1 showcircle5");
					// 检测器动画完成时 风关闭
					$(".page6 .p6_circle4").get(0).addEventListener("webkitAnimationEnd",function(){
						$(".page6 .mask").fadeIn();
						setTimeout(function(){
							$(".p6_phone").show();
							p6_phone();
						},1000);
					},false);
				},500);
			},2500);
		},3000);
	}
	function p6_phone(){
		var time5 = null;
		var beginNum = 200;
		var maxT = 500;
		time5 = setInterval(function(){
			beginNum+=5;
			if(beginNum<=maxT){
				$(".page6 .pmvalue").html(beginNum);
			}else{
				clearInterval(time5);
				$(".p6_loading").removeClass("loadingrotate");
				setTimeout(function(){
					$(".p6_loading").fadeOut();
					$(".p6_jianceing").fadeOut();
					$(".p6_wuran").fadeIn();
					$(".p6_jiance2").fadeIn();
					$(".p6_sugg2").addClass("fadeInword");
					$(".p6_btn").click(function(){
						$(".p6_phone").addClass("slideOutRightP");
						$(".p6_phone").get(0).addEventListener("webkitAnimationEnd",function(){
							$(".p6_windl").css("opacity","1");
			                $(".p6_windt").css("opacity","1");
			                $(".con10").addClass("fadeInOutC");
			                $(".p6_phone").remove();
			                $(".con10").get(0).addEventListener("webkitAnimationEnd",function(){
								$(".page6 .mask").fadeOut();
								setTimeout(function(){
									$(".page6").fadeOut();
								    $(".page7").fadeIn();
								},1500);
							},false);
						},false);
					});
				},1000);
			}
		},40)
	}
	// page6();
	// page7
	$(".page7").on("touchmove",function(){
		$(".page8").show();
		$(".page7").hide();
	});
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
	var regName = /^[\u4e00-\u9fa5]*$/;
	// 电话号码的验证 手机号
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
				url:"http://192.168.0.17:4000/presell",
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