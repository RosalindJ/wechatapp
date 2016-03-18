(function () {
    $(".section").height($(window).height());
    var r = $(".oneGerm");
    var o = $(".twoGerm");
    var L = $(".dust");
    var E = $(".anion");
    var k = [{
            ow: 40,
            oh: 43,
            url: "img/germ7.png"
        }, {
            ow: 47,
            oh: 47,
            url: "img/germ6.png"
        }];
    var N = [];
    (function () {
        for (var R = 1; R <= $(".page1 canvas").length; R++) {
            (function (S) {
                var T = {
                    canvasId: "canvas_" + S + "",
                    h: k[S - 1].ow * 2,
                    w: k[S - 1].oh * 2,
                    ox: 0,
                    oy: 0,
                    imgUrl: k[S - 1].url,
                    width: k[S - 1].ow,
                    height: k[S - 1].oh,
                };
                N[R - 1] = T
            })(R)
        }
    })();
 
    function G(T) {
        var S = document.getElementById(T);
        var R = S.getContext("2d");
        R.clearRect(0, 0, S.width, S.height)
    }
    function n(R) {
        $(R).removeClass("top_bottom_show opacity").addClass("top_bot_hide")
    }
    function x(R) {
        $(R).removeClass("top_bot_hide").addClass("top_bottom_show")
    }
    function s(R) {
        $(R).removeClass("opacity top_bottom_show").addClass("opacity_hide")
    }
    function z(R) {
        $(R).removeClass("opacity_hide").addClass("opacity")
    }
    function F() {
        for (var R = 1; R <= r.length; R++) {
            r.eq(R - 1).removeClass("animate center_" + R + "").addClass("animated_1 top_bottom_hide")
        }
        setTimeout(function () {
            $(".bg2").stop().animate({
                opacity: 1
            }, 1000, function () {
                w = true
            });
            n(".clear_1");
            z(".clear_2");
            s(".word_1");
            z(".word_2")
        }, 200)
    }
    function D(R) {
        o.eq(R - 1).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", function () {
            if (A) {
                o.find("canvas").show();
                N[R - 1].isStart = true;
                o.eq(R - 1).fragment(N[R - 1]);
                (function (S) {
                    setTimeout(function () {
                        o.eq(S - 1).find("img").hide()
                    }, 100)
                })(R)
            }
        })
    }
    var A = true;
 
    function p() {
        A = true;
        for (var S = 1; S <= o.length; S++) {
            o.eq(S - 1).removeClass("animate center_" + (S + 5) + "").addClass("animated_2 top_bottom_" + S + "")
        }
        for (var R = 1; R <= o.length; R++) {
            D(R)
        }
        setTimeout(function () {
            $(".bg3").stop().animate({
                opacity: 1
            }, 1000, function () {
                w = true;
                for (var T = 1; T <= $("canvas").length; T++) {
                    G("canvas_" + T + "")
                }
            });
            n(".clear_2");
            z(".clear_3");
            s(".word_2");
            z(".word_3")
        }, 800)
    }
    function i() {
        for (var R = 1; R <= L.length; R++) {
            if (R < 5) {
                L.eq(R - 1).removeClass("animate dust_1").addClass("animated_3 dust1_hide")
            } else {
                if (R >= 5 && R < 9) {
                    L.eq(R - 1).removeClass("animate dust_2").addClass("animated_3 dust2_hide")
                } else {
                    if (R >= 9 && R < 13) {
                        L.eq(R - 1).removeClass("animate dust_3").addClass("animated_3 dust3_hide")
                    } else {
                        if (R >= 13 && R < 17) {
                            L.eq(R - 1).removeClass("animate dust_4").addClass("animated_3 dust4_hide")
                        } else {
                            if (R >= 17 && R < 22) {
                                L.eq(R - 1).removeClass("animate dust_1").addClass("animated_3 dust5_hide")
                            } else {
                                L.eq(R - 1).removeClass("animate dust_2").addClass("animated_3 dust6_hide")
                            }
                        }
                    }
                }
            }
        }
        $(".bg4").stop().animate({
            opacity: 1
        }, 1000, function () {
            y()
        });
        n(".clear_3");
        z(".anion_word");
        s(".word_3");
        z(".machine")
    }
    var g = new Array();
 
    function y() {
        var T = E.length;
        for (var R = 1; R <= E.length; R++) {
            g[R - 1] = true;
            E.eq(R - 1).removeClass("anionrun1 anionrun2 anionBottom" + R + "").addClass("anionTop" + R + "").css({
                opacity: 1
            })
        }
        for (var S = 1; S <= T; S++) {
            (function (U) {
                E.eq(U - 1).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", function () {
                    if (g[U - 1]) {
                        g[U - 1] = false;
                        var V = "animated_2 anionTop" + U;
                        if (Math.random() > 0.5) {
                            $(this).removeClass(V).addClass("animated anionrun1")
                        } else {
                            $(this).removeClass(V).addClass("animated anionrun2")
                        } if (U == T) {
                            w = true
                        }
                    }
                })
            })(S)
        }
    }
    function h() {
        n(".anion_word");
        z(".water_word");
        s(".machine");
        z(".water");
        setTimeout(function () {
            w = true
        }, 1000)
    }
    var P = true;
 
    function d() {
        n(".water_word");
        z(".temper_word");
        s(".water");
        $(".sun").removeClass("animated opacity_hide").addClass("sunFadeInOut");
        P = true;
        $(".sun").one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", function () {
            if (P) {
                P = false;
                $(".sun").removeClass("sunFadeInOut").addClass("animate opac_1");
                w = true
            }
        })
    }
    var l = [];
 
    function M() {
        n(".temper_word");
        z(".oxygen_word");
        $(".oxygen").css({
            opacity: 1
        });
        for (var R = 1; R <= $(".oxygen").length; R++) {
            $(".oxygen").eq(R - 1).removeClass("animated_3 scaleHide").addClass("animated_1 oxygenLeft" + R + "")
        }
        var T = $(".oxygen").length;
        for (var S = 1; S <= T; S++) {
            l[S - 1] = true;
            (function (U) {
                $(".oxygen").eq(U - 1).one(
                    "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", function () {
                    if (l[U - 1]) {
                        l[U - 1] = false;
                        var V = "animated_1 oxygenLeft" + U;
                        if (Math.random() > 0.5) {
                            $(this).removeClass(V).addClass("animated oxygenrun1")
                        } else {
                            $(this).removeClass(V).addClass("animated oxygenrun2")
                        } if (U == T) {
                            w = true
                        }
                    }
                })
            })(S)
        }
    }
    function u() {
        setTimeout(function () {
            $(".oxygen_word").hide()
        }, 200);
        x(".freshAirWord");
        $(".page2").stop(0).animate({
            opacity: 1
        }, 1000, function () {
            w = true;
        })
    }
    function K() {
        $(".bg2").stop().animate({
            opacity: 0
        }, 1000);
        x(".clear_1");
        s(".clear_2");
        z(".word_1");
        s(".word_2");
        for (var R = 1; R <= r.length; R++) {
            r.eq(R - 1).removeClass("animated_1 top_bottom_hide").addClass("animated_1 top_bot_show")
        }
        setTimeout(function () {
            for (var S = 1; S <= r.length; S++) {
                r.eq(S - 1).removeClass("animated_1 top_bot_show").addClass("animate center_" + S + "")
            }
            w = true
        }, 600)
    }
    function q() {
        $(".bg3").stop().animate({
            opacity: 0
        }, 1000, function () {
            w = true
        });
        A = false;
        o.find("canvas").hide();
        o.find("img").show();
        setTimeout(function () {
            x(".clear_2");
            s(".clear_3");
            z(".word_2");
            s(".word_3");
            for (var R = 1; R <= o.length; R++) {
                o.eq(R - 1).removeClass("animated_2 top_bottom_" + R + "").addClass("animated_2 bottomTop_" + R + "")
            }
        }, 200);
        setTimeout(function () {
            for (var R = 1; R <= o.length; R++) {
                o.eq(R - 1).removeClass("animated_2 bottomTop_" + R + "").addClass("animate center_" + (R + 3) + "")
            }
        }, 1000)
    }
    function C(R, T, S) {
        L.eq(R - 1).removeClass("animated_3 dust" + T + "_hide").addClass("animated dust_show");
        (function (U) {
            setTimeout(function () {
                if (I[U - 1]) {
                    I[U - 1] = false;
                    L.eq(U - 1).removeClass("animated dust_show").addClass("animate dust_" + S + "");
                    if (U == L.length) {
                        w = true
                    }
                }
            }, 1500)
        })(R)
    }
    var I = [];
 
    function f() {
        $(".bg4").stop().animate({
            opacity: 0
        }, 1000);
        x(".clear_3");
        s(".anion_word");
        z(".word_3");
        s(".machine");
        for (var S = 1; S <= E.length; S++) {
            E.eq(S - 1).removeClass("anionrun1 anionrun2").addClass("anionBottom" + S + "")
        }
        for (var R = 1; R <= L.length; R++) {
            I[R - 1] = true
        }
        setTimeout(function () {
            for (var T = 1; T <= L.length; T++) {
                if (T < 5) {
                    C(T, 1, 1)
                } else {
                    if (T >= 5 && T < 9) {
                        C(T, 2, 2)
                    } else {
                        if (T >= 9 && T < 13) {
                            C(T, 3, 3)
                        } else {
                            if (T >= 13 && T < 17) {
                                C(T, 4, 4)
                            } else {
                                if (T >= 17 && T < 22) {
                                    C(T, 5, 1)
                                } else {
                                    C(T, 6, 2)
                                }
                            }
                        }
                    }
                }
            }
        }, 500)
    }
    function j() {
        x(".anion_word");
        s(".water_word");
        z(".machine");
        s(".water");
        setTimeout(function () {
            w = true
        }, 1200)
    }
    function Q() {
        x(".water_word");
        s(".temper_word");
        z(".water");
        $(".sun").removeClass("animate opac_1 sunFadeInOut").addClass("animated opacity_hide");
        setTimeout(function () {
            w = true
        }, 1000)
    }
    function m() {
        x(".temper_word");
        s(".oxygen_word");
        for (var R = 0; R < $(".oxygen").length; R++) {
            $(".oxygen").eq(R).removeClass("animated oxygenrun1 oxygenrun2").addClass("animated_3 scaleHide")
        }
        setTimeout(function () {
            w = true
        }, 2000)
    }
    function t() {
        $(".oxygen_word").show();
        n(".freshAirWord");
        $(".page2").stop(0).animate({
            opacity: 0
        }, 1000, function () {
            w = true
        })
    }
    function v() {
        $.fn.fullpage.setAllowScrolling(true);
        w = true;
    }
    function v_1() {
        var gap = $("#fullpage").height() - $(window).height();
        $("#fullpage").css({webkitTransform: "translate3d(0px, -"+gap+"px, 0px)",transform: "translate3d(0px, -"+gap+"px, 0px)"});
        // $.fn.fullpage.setAllowScrolling(true);
        w = true;
    }
    var w = true;
    var b = 0;
    var tt = false;
    function B(R) {
        if (w) {
            if (R) {
                b++;
                if(b > 8){
                    b = 8;
                }
                if(b < 8){
                	$(".animateList span").removeClass("animateListActive").eq(b).addClass("animateListActive");
                }
                w = false;
                switch (b) {
                case 1:
                    F();
                    break;
                case 2:
                    p();
                    break;
                case 3:
                    i();
                    break;
                case 4:
                    h();
                    break;
                case 5:
                    d();
                    break;
                case 6:
                    M();
                    break;
                case 7:
                    u();
                    break;
                case 8:
                    v_1();
                    break
                }
            } else {
                b--;
                w = false;
                $(".animateList span").removeClass("animateListActive").eq(b).addClass("animateListActive");
                switch (b) {
                case -1:
                    v();
                    break;
                case 0:
                    K();
                    break;
                case 1:
                    q();
                    break;
                case 2:
                    f();
                    break;
                case 3:
                    j();
                    break;
                case 4:
                    Q();
                    break;
                case 5:
                    m();
                    break;
                case 6:
                    t();
                    break;
                case 7:(function(){
                        var gap = ($(".section").length-1)*$(window).height();
                        $("#fullpage").css({webkitTransform: "translate3d(0px, -"+gap+"px, 0px)",transform: "translate3d(0px, -"+gap+"px, 0px)"});
                        setTimeout(function(){w = true;},500);
                        
                     }());break;
                }
                
            }
        }
    }
    function c() {
        document.onmousewheel = function (R) {
            var R = R || window.event;
            R.preventDefault();
            B(R.wheelDelta < 0)
        };
        if (document.addEventListener) {
            document.addEventListener("DOMMouseScroll", function (R) {
                var R = R || window.event;
                R.preventDefault();
                B(R.detail > 0)
            })
        }
    }
    var H = null;
    var O = -100;
 
    function e() {
        $("#text h1").show();
        H = setInterval(function () {
            O += 2;
            if (O > 100) {
                clearInterval(H)
            } else {
                $("#text h1").css({
                    backgroundImage: "-moz-linear-gradient(#fff,#fff)",
                    backgroundImage: "linear-gradient(#444 " + O + "%,#fff)"
                })
            }
        }, 15)
    }
    $("#fullpage").fullpage({
        verticalCentered: false,
        easing: "easeInOutCubic",
        navigation: true,
        navigationPosition: "right",
        afterLoad: function (S, R) {
            switch (R) {
            case 1:
                (function () {
                    $("#fp-nav").show();
                    $(".animateList span").removeClass("animateListActive").eq(0).addClass("animateListActive");
                }());
                break;
            case 2:
                (function () {
                    $("#fp-nav").show();
                    $(".animateList span").removeClass("animateListActive").eq(0).addClass("animateListActive");
                    e();
                }());
                break;
            case 3:
                (function () {
                    $.fn.fullpage.setAllowScrolling(false);
                    if (b < 0) {
                        b = 0;
                    } 
                    w = true;
                    c();
                    $("#fp-nav").hide();
                }());
                break;
            case 4:
                (function () {
                    $("#fp-nav").show();
                }());
                break
            }
        }
    });
 
    function a() {
        $("video").eq(0).get(0).pause()
    }
    function J(R, T, S) {
        R.on("click", function () {
            $(".mask").eq(S).show();
            T.get(0).play();
            R.hide()
        })
    }
    J($(".play:eq(0)"), $("video:eq(0)"), 0);
}());