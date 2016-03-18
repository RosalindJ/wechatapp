(function () {
    var j = $("#nav").height();
    var g = [$("#page_2").offset().top - 2 * j, $("#page_3").offset().top - 2 * j, 4178, 5264];
 
    function i(l, k) {
        $(".secondList li").eq(l).find("a").on("click", function (m) {
            $("html,body").stop().animate({
                scrollTop: $("#page_" + k + "").offset().top - $(".secondList").height()
            }, 1000)
        })
    }
    i(0, 1);
    i(1, 2);
    i(2, 3);
    i(3, 4);
    i(4, 5);
    i(5, 6);
    i(6, 7);
 
    function a(m, l, k, o, p) {
        var n = p || null;
        setTimeout(function () {
            $(".arrow_" + m + "").show();
            $(".arrow_" + l + "").show();
            $(".line_" + k + "").show();
            $(".detailText_" + k + "").show();
            if (n) {
                $(".line_" + p + "").show();
                $(".detailText_" + p + "").show()
            }
        }, o)
    }
    function h(k) {
        $(".tabBnt").eq(k).on("click", function () {
            $(".technologyBntBg").hide();
            $(".feelBntBg").hide();
            if ($(".feelBnt").eq(k).css("display") != "none") {
                $(".technology").eq(k).hide();
                $(".feel").eq(k).show();
                $(".technologyBnt").eq(k).show();
                $(".feelBnt").eq(k).hide()
            } else {
                $(".technology").eq(k).show();
                $(".feel").eq(k).hide();
                $(".technologyBnt").eq(k).hide();
                $(".feelBnt").eq(k).show()
            }
        })
    }
    h(0);
    h(1);
    h(2);
    var b = true;
    var c = true;
    var e = true;
 
    function d() {
        $(window).on("scroll", function () {
            $("#nav .topList").slideUp();
            if ($(window).scrollTop() == 0) {
                $("#nav .topList").slideDown()
            }
            if ($(window).scrollTop() > g[0] && b) {
                b = false;
                $(".productInside_1").addClass("move_open_1");
                $(".productInside_2").addClass("move_open_2");
                a(3, 2, 3, 1000);
                a(5, 6, 4, 2000, 2);
                a(1, 4, 1, 3000)
            }
            if ($(window).scrollTop() > g[1] && c) {
                c = false;
                $(".windImg").addClass("pushWind")
            }
        })
    }
    d();
    var f = {
        element: ".bg_6",
        pos_1: g[2],
        pos_2: g[3],
        spacing: 10,
        maxTop: -120,
    };
    $("#page_6").translateBg(f, e)
}());