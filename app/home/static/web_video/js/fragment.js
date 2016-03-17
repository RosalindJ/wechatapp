(function (a) {
    a.fn.fragment = function (l) {
        var g = {
            canvasId: "canvas",
            h: 400,
            w: 400,
            ox: 0,
            oy: 0,
            imgUrl: "",
            width: 200,
            height: 200,
            isStart: false,
        };
        var t = a.extend(g, l);
        var e = a(this);
        var f;
        var b;
        var v;
        var d = 1;
        var c;
        var q = new Array();
        var u = new Array();
        var k = new Array();
        var m = u;
        var h = null;
        for (var r = 0; r < t.h; r++) {
            u[r] = new Array();
            k[r] = new Array();
            for (var p = 0; p < t.w; p++) {
                u[r][p] = {
                    x: t.ox + p,
                    y: t.oy + r
                };
                k[r][p] = {
                    x: t.ox + p,
                    y: t.oy + r,
                    vx: 0,
                    vy: 0,
                    ax: 0.16 - Math.random() * 0.08,
                    ay: 0.16 - Math.random() * 0.08,
                    nx: 0.4 + Math.random() * 0.3,
                    ny: 0.3 + Math.random() * 0.2
                }
            }
        }
        s();
 
        function s() {
            f = document.getElementById(t.canvasId);
            b = f.getContext("2d");
            c = f.height - 1;
            v = new Image();
            v.src = t.imgUrl;
            v.onload = function () {
                b.clearRect(0, 0, f.width, f.height);
                b.drawImage(v, 0, 0, t.width, t.width);
                for (var x = 0; x < t.h; x++) {
                    q[x] = [];
                    for (var w = 0; w < t.w; w++) {
                        q[x][w] = b.getImageData(w, x, 1, 1)
                    }
                }
            }
        }
        function n() {
            b.clearRect(0, 0, f.width, f.height);
            setTimeout(function () {
                clearInterval(h)
            }, 2000);
            for (var x = t.h - 1; x > 0; x--) {
                for (var w = t.h - 1; w > 0; w--) {
                    var y = k[x][w];
                    y.x += y.vx;
                    y.y += y.vy;
                    if (y.y >= c) {
                        y.y = c;
                        y.vy = -y.ny * y.vy;
                        if (Math.abs(y.vy) <= 1) {
                            y.vy = 0
                        }
                        y.vx *= y.nx;
                        if (Math.abs(y.vx) <= 1) {
                            y.vx = 0
                        }
                    } else {
                        y.vy += 1
                    }
                    q[x][w].data[3] -= 8;
                    b.putImageData(q[x][w], y.x, y.y)
                }
            }
        }
        o();
 
        function o() {
            if (t.isStart) {
                for (var x = 0; x < t.h; x++) {
                    for (var w = 0; w < t.w; w++) {
                        var y = k[x][w];
                        y.vx = (Math.random() - Math.random()) * 5;
                        y.vy = -Math.random() * 2
                    }
                }
                h = setInterval(n, 5)
            }
        }
    }
})(jQuery);