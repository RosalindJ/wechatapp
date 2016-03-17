(function () {
    var g = [824, 3660, 4418, $("#page_6").offset().top-$("#nav").height()];
    $(".text_1").playWords();
    var a = [{
            oh: 100,
            ol: 590
        }, {
            oh: 146,
            ol: 362
        }, {
            oh: 230,
            ol: 212
        }, {
            oh: 250,
            ol: 94
        }, {
            oh: 170,
            ol: -22
        }];
    var i = [0, 700, 1200, 1700, 2200];
 
    function f(l) {
        $(".wrapText").find(".detailText").hide().eq(l).show();
        $(".leader").hide().css({
            height: a[l].oh,
            left: a[l].ol
        });
        $(".leadImg").stop().animate({
            left: a[l].ol
        }, 200, function () {
            $(".leader").show()
        })
    }
    function j() {
        $(".wrapText").show();
        $(".leadImg").show();
        $(".leader").show();
        $(".blue").show();
        $(".arrow").show();
        for (var l = 0; l < a.length; l++) {
            (function (m) {
                setTimeout(function () {
                    f(m)
                }, i[m])
            })(l)
        }
    }
    var k = 0;
 
    function h() {
        setTimeout(function () {
            j();
            setTimeout(function () {
                $(".touch").mouseover(function () {
                    f($(this).index() - $("#product").children().length + $(".touch").length)
                })
            }, i[i.length - 1])
        }, 400);
        setInterval(function () {
            $(".touch").removeClass("opac_1").css({
                boxShadow: ""
            }).eq(k).addClass("opac_1").css({
                boxShadow: "4px 4px 30px #FFF,-4px -4px 30px #fff"
            });
            k++;
            if (k > $(".touch").length - 1) {
                k = 0
            }
        }, 3000)
    }
    var b = true;
    var c = true;
 
    function d() {
        $(window).on("scroll", function () {
            var l = $(window).scrollTop();
            if (l > g[0] && b) {
                b = false;
                $("#product").addClass("scaleSmall");
                setTimeout(function () {
                    $(".titel_2").hide();
                    $(".lid_2").addClass("openLid_2");
                    $(".lid_1").addClass("openLid_1");
                    // setTimeout(function(){})
                    var image = new Image();
                    image.src = "img/trendy/lid_2.png";
                    image.onload = function(){
                        $(".lid_2").find("img").attr("src", image.src);
                        $(".lid_2").css({
                            top: -17,
                            width: "16%"
                        });
                    }
                    
                    h()
                }, 1000)
            }
            if (l > g[3] && c) {
                c = false;
                $(".phone").addClass("fadeRightIn")
            }
        })
    }
    d();
    var e = {
        element: ".bg_5",
        pos_1: g[1],
        pos_2: g[2],
        spacing: 20,
        maxTop: -120,
    };
    var c = true;
    $("#page_5").translateBg(e, c)
}());