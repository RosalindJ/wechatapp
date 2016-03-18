(function (a) {
    a.fn.translateBg = function (f, g) {
        var e = {
            element: ".translateBg",
            pos_1: 0,
            pos_2: 0,
            spacing: 10,
            maxTop: -120,
        };
        var h = a.extend(e, f);
        var c = g || true;
        var d = parseInt(h.pos_1);
        var b = null;
        a(window).on("scroll", function () {
            var i = a(window).scrollTop();
            if (i > h.pos_1 && c && i < h.pos_2) {
                b = i;
                var j = parseInt(a(h.element).css("top"));
                if (b - d > 0 && j < 0) {
                    c = false;
                    a(h.element).stop().animate({
                        top: j + h.spacing
                    }, 1000, function () {
                        c = true
                    })
                } else {
                    if (j > h.maxTop) {
                        c = false;
                        a(h.element).stop().animate({
                            top: j - h.spacing
                        }, 1000, function () {
                            c = true
                        })
                    }
                }
                d = b
            }
        })
    }
})(jQuery);