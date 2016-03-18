(function (a) {
    a.fn.playWords = function (e) {
        var d = {
            sunId: "biao",
            arr: ["净化更强？", "更加智能？", "体积更小？"],
            position: "keyWords",
            speed: 500,
            sunSpeed: 500,
        };
        var f = a.extend(d, e);
 
        function b() {
            var h = a("#" + f.sunId + "");
            var g = true;
            setInterval(function () {
                if (g) {
                    g = false;
                    h.hide()
                } else {
                    g = true;
                    h.show()
                }
            }, f.sunSpeed)
        }
        b();
 
        function c() {
            var j = 0;
            var k = 0;
            var h = true;
            var g = a("#" + f.position + "");
            setInterval(function () {
                if (h) {
                    j++;
                    if (j <= f.arr[k].length) {
                        g.html(f.arr[k].substring(0, j))
                    } else {
                        h = false;
                        j = f.arr[k].length
                    }
                } else {
                    j--;
                    if (j > 0) {
                        g.html(f.arr[k].substring(0, j))
                    } else {
                        if (j == 0) {
                            g.html("")
                        } else {
                            h = true;
                            j = 0;
                            k++;
                            if (k > f.arr.length - 1) {
                                k = 0
                            }
                        }
                    }
                }
            }, f.speed)
        }
        c()
    }
})(jQuery);