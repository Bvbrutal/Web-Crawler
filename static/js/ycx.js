IOyA = function (t, e, n) {
    "use strict";
    (function (t, a) {
        var i,
            r = n("Dd8w"),
            o = n.n(r),
            s = n("mvHQ"),
            u = n.n(s),
            c = n("Xxa5"),
            l = n.n(c),
            d = n("exGp"),
            p = n.n(d),
            f = n("Zrlr"),
            _ = n.n(f),
            h = n("wxAW"),
            m = n.n(h),
            g = n("L6bb"),
            v = n.n(g),
            S = n("Av7u"),
            T = n.n(S),
            y = n("oMTx"),
            R = n("1ANT"),
            w = n("IuJc"),
            C = (n.n(w), new (n("4C6m").JSEncrypt)()),
            D = new R.a("sessionStorage"),
            A = (function () {
                function e() {
                    _()(this, e),
                        (this.appInfo = {}),
                        (this.baseUrl = w.dev.baseUrl || ""),
                        (this.signatureInfo = {});
                }

                return (
                    m()(e, [
                        {
                            key: "getNonce",
                            value: function (t) {
                                t = t || 32;
                                for (
                                    var e =
                                            "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678",
                                        n = e.length,
                                        a = "",
                                        i = 0;
                                    i < t;
                                    i++
                                )
                                    a += e.charAt(Math.floor(Math.random() * n));
                                return a;
                            },
                        },
                        {
                            key: "getTimestamp",
                            value: function () {
                                return new Date().getTime();
                            },
                        },
                        {
                            key: "getSignatureInfo",
                            value: function () {
                                return {
                                    appId: "846a15365f614921a5617cd1c2478129",
                                    appKey:
                                        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkVxSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvozJQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiHpz0vAGktjO0RaN2tzwIDAQAB",
                                };
                            },
                        },
                        {
                            key: "getToken",
                            value: (function () {
                                var e = p()(
                                    l.a.mark(function e() {
                                        var n, a, i;
                                        return l.a.wrap(
                                            function (e) {
                                                for (; ;)
                                                    switch ((e.prev = e.next)) {
                                                        case 0:
                                                            return (
                                                                (n = void 0),
                                                                    (e.next = 3),
                                                                    this.getConfig(url, {})
                                                            );
                                                        case 3:
                                                            return (
                                                                (a = e.sent),
                                                                    (i = void 0),
                                                                    (e.prev = 5),
                                                                    (e.next = 8),
                                                                    t(a)
                                                            );
                                                        case 8:
                                                            (i = e.sent), (e.next = 14);
                                                            break;
                                                        case 11:
                                                            (e.prev = 11),
                                                                (e.t0 = e.catch(5)),
                                                                console.log(e.t0);
                                                        case 14:
                                                            return (
                                                                (n =
                                                                    200 === i.status && i.data.success
                                                                        ? i.data
                                                                        : ""),
                                                                    e.abrupt("return", n)
                                                            );
                                                        case 16:
                                                        case "end":
                                                            return e.stop();
                                                    }
                                            },
                                            e,
                                            this,
                                            [[5, 11]]
                                        );
                                    })
                                );
                                return function () {
                                    return e.apply(this, arguments);
                                };
                            })(),
                        },
                        {
                            key: "reLogin",
                            value: function () {
                                y.a.page.appear({
                                    success: function (t) {
                                        "true" == window.bwtRelogin && window.location.reload();
                                    },
                                    error: function (t) {
                                    },
                                }),
                                    (window.bwtRelogin = "true"),
                                    vm.$vux.confirm.show({
                                        title: "登录已失效",
                                        content: "请重新登录以保证正常使用",
                                        confirmText: "重新登录",
                                        cancelText: "取消",
                                        onCancel: function () {
                                            y.a.page.pop();
                                        },
                                        onConfirm: function () {
                                            window.sessionStorage.removeItem("userInfo"),
                                                y.a.page.push({
                                                    url: "BWTLoginPage",
                                                    pageTitle: "",
                                                    orientation: "",
                                                    params: {title: "", pageUrl: ""},
                                                    success: function (t) {
                                                    },
                                                    error: function (t) {
                                                        console.log("失败:" + u()(t));
                                                    },
                                                });
                                        },
                                    });
                            },
                        },
                        {
                            key: "upLoadImgBase64",
                            value: (function () {
                                var t = p()(
                                    l.a.mark(function t(e, n, a, i) {
                                        var r, o, s;
                                        return l.a.wrap(
                                            function (t) {
                                                for (; ;)
                                                    switch ((t.prev = t.next)) {
                                                        case 0:
                                                            (r = n.split("base64,")[1]),
                                                                (o = "https://up.qbox.me/putb64/-1"),
                                                                (s = new XMLHttpRequest()).open(
                                                                    "POST",
                                                                    o,
                                                                    !0
                                                                ),
                                                                s.setRequestHeader(
                                                                    "Content-Type",
                                                                    "application/octet-stream"
                                                                ),
                                                                s.setRequestHeader(
                                                                    "Authorization",
                                                                    "UpToken " + e
                                                                ),
                                                                s.send(r),
                                                                (s.onreadystatechange = function () {
                                                                    4 == s.readyState && a(s);
                                                                });
                                                        case 8:
                                                        case "end":
                                                            return t.stop();
                                                    }
                                            },
                                            t,
                                            this
                                        );
                                    })
                                );
                                return function (e, n, a, i) {
                                    return t.apply(this, arguments);
                                };
                            })(),
                        },
                        {
                            key: "getSequence",
                            value: function () {
                                for (
                                    var t = a().format("YYYYMMDDHHmmss"), e = "", n = 0;
                                    n < 10;
                                    n++
                                )
                                    e += Math.floor(10 * Math.random());
                                return t + e;
                            },
                        },
                        {
                            key: "getApiUrl",
                            value: function () {
                                return window.location.href.split("/app-h5")[0];
                            },
                        },
                        {
                            key: "getLocationUrl",
                            value: function () {
                                return (
                                    window.location.href.split("/app-h5")[0] + "/app-h5/"
                                );
                            },
                        },
                        {
                            key: "getConfig",
                            value: (function () {
                                var t = p()(
                                    l.a.mark(function t(e) {
                                        var n,
                                            a,
                                            i,
                                            r =
                                                arguments.length > 1 && void 0 !== arguments[1]
                                                    ? arguments[1]
                                                    : {};
                                        return l.a.wrap(
                                            function (t) {
                                                for (; ;)
                                                    switch ((t.prev = t.next)) {
                                                        case 0:
                                                            return (
                                                                (n = this.baseUrl
                                                                    ? this.baseUrl
                                                                    : this.getApiUrl()),
                                                                    (t.next = 3),
                                                                    this.getHeaders(r)
                                                            );
                                                        case 3:
                                                            return (
                                                                (a = t.sent),
                                                                    (i = {
                                                                        method: "post",
                                                                        url: n + e,
                                                                        data: r,
                                                                        timeout: 3e6,
                                                                        headers: a,
                                                                    }),
                                                                    t.abrupt("return", i)
                                                            );
                                                        case 6:
                                                        case "end":
                                                            return t.stop();
                                                    }
                                            },
                                            t,
                                            this
                                        );
                                    })
                                );
                                return function (e) {
                                    return t.apply(this, arguments);
                                };
                            })(),
                        },
                        {
                            key: "getHeaders",
                            value: (function () {
                                var t = p()(
                                    l.a.mark(function t() {
                                        var e,
                                            n,
                                            a,
                                            i,
                                            r,
                                            o,
                                            s,
                                            u =
                                                arguments.length > 0 && void 0 !== arguments[0]
                                                    ? arguments[0]
                                                    : {};
                                        return l.a.wrap(
                                            function (t) {
                                                for (; ;)
                                                    switch ((t.prev = t.next)) {
                                                        case 0:
                                                            return (
                                                                (e = void 0),
                                                                    (n = this.getNonce()),
                                                                    (a = this.getTimestamp()),
                                                                    (t.next = 5),
                                                                    this.getSignature(u, !0, n, a)
                                                            );
                                                        case 5:
                                                            return (
                                                                (i = t.sent),
                                                                    (t.next = 8),
                                                                    y.a.user.getToken()
                                                            );
                                                        case 8:
                                                            if (((t.t0 = t.sent), t.t0)) {
                                                                t.next = 11;
                                                                break;
                                                            }
                                                            t.t0 = {};
                                                        case 11:
                                                            return (
                                                                (r = t.t0),
                                                                    (o = r.token),
                                                                    (t.next = 16),
                                                                    y.a.runtime.getCityInfo()
                                                            );
                                                        case 16:
                                                            return (
                                                                ((s = t.sent) && s.cityId) ||
                                                                console.log("token为空"),
                                                                    (e = {
                                                                        appid: this.appInfo.appId,
                                                                        token: o || "",
                                                                        cityId:
                                                                            (s && s.cityId) ||
                                                                            this.appInfo.cityId ||
                                                                            "5000",
                                                                        bundleId: this.appInfo.bundleId || "",
                                                                        "X-Ca-Version": "v1.0",
                                                                        random: "",
                                                                        sequence: this.getSequence(),
                                                                        app_version: this.appInfo.version || "",
                                                                        signature: i,
                                                                        "X-Ca-Signature-Version": "1",
                                                                        nonce: n,
                                                                        timestamp: a,
                                                                        "Content-Type":
                                                                            "application/json;charset=utf-8",
                                                                        Accept: "application/json",
                                                                    }),
                                                                    t.abrupt("return", e)
                                                            );
                                                        case 20:
                                                        case "end":
                                                            return t.stop();
                                                    }
                                            },
                                            t,
                                            this
                                        );
                                    })
                                );
                                return function () {
                                    return t.apply(this, arguments);
                                };
                            })(),
                        },
                        {
                            key: "getQueryString",
                            value: function (t) {
                                var e = new RegExp(t + "=([^&]*)(&|$)", "i"),
                                    n = window.location.href.match(e);
                                return null != n ? n[1] : "";
                            },
                        },
                        {
                            key: "initAppInfo",
                            value: (function () {
                                var e = p()(
                                    l.a.mark(function e() {
                                        var n, a, i, r, s, c;
                                        return l.a.wrap(
                                            function (e) {
                                                for (; ;)
                                                    switch ((e.prev = e.next)) {
                                                        case 0:
                                                            return (e.next = 2), y.a.runtime.getAppInfo();
                                                        case 2:
                                                            if (((e.t0 = e.sent), e.t0)) {
                                                                e.next = 5;
                                                                break;
                                                            }
                                                            e.t0 = {};
                                                        case 5:
                                                            if ((n = e.t0) && n.appId && n.publicKey) {
                                                                e.next = 21;
                                                                break;
                                                            }
                                                            if (!(a = D.get("appInfoConfig"))) {
                                                                e.next = 12;
                                                                break;
                                                            }
                                                            (e.t1 = {data: a}), (e.next = 15);
                                                            break;
                                                        case 12:
                                                            return (
                                                                (e.next = 14),
                                                                    t.get(
                                                                        "https://bwton-cdn.oss-cn-shanghai.aliyuncs.com/app-info/config.json"
                                                                    )
                                                            );
                                                        case 14:
                                                            e.t1 = e.sent;
                                                        case 15:
                                                            (i = e.t1),
                                                                (r = i.data),
                                                                D.set("appInfoConfig", u()(r)),
                                                                (s = this.getQueryString("bundleId")),
                                                                (c = r[s] ? r[s] : r.default),
                                                                (n = o()({bundleId: s}, c, {
                                                                    appId: T.a.AES.decrypt(
                                                                        c.appId,
                                                                        "bwton@123"
                                                                    ).toString(T.a.enc.Utf8),
                                                                    publicKey: T.a.AES.decrypt(
                                                                        c.appKey,
                                                                        "bwton@123"
                                                                    ).toString(T.a.enc.Utf8),
                                                                }));
                                                        case 21:
                                                            this.appInfo = o()({}, n, {
                                                                appId: n.appId,
                                                                appKey: n.publicKey,
                                                            });
                                                        case 22:
                                                        case "end":
                                                            return e.stop();
                                                    }
                                            },
                                            e,
                                            this
                                        );
                                    })
                                );
                                return function () {
                                    return e.apply(this, arguments);
                                };
                            })(),
                        },
                        {
                            key: "getSignature",
                            value: (function () {
                                var t = p()(
                                    l.a.mark(function t() {
                                        var e,
                                            n,
                                            a,
                                            i =
                                                arguments.length > 0 && void 0 !== arguments[0]
                                                    ? arguments[0]
                                                    : {},
                                            r =
                                                arguments.length > 1 &&
                                                void 0 !== arguments[1] &&
                                                arguments[1],
                                            o = arguments[2],
                                            s = arguments[3];
                                        return l.a.wrap(
                                            function (t) {
                                                for (; ;)
                                                    switch ((t.prev = t.next)) {
                                                        case 0:
                                                            return (t.next = 2), this.initAppInfo();
                                                        case 2:
                                                            return (
                                                                (this.signatureInfo = this.appInfo),
                                                                    (e = u()(i)),
                                                                    (n = void 0),
                                                                    (n = r
                                                                        ? "appid=" +
                                                                        this.signatureInfo.appId +
                                                                        "&message=" +
                                                                        e +
                                                                        "&nonce=" +
                                                                        o +
                                                                        "&timestamp=" +
                                                                        s
                                                                        : e),
                                                                    console.log(n),
                                                                    (a = (a = v()(n)).toUpperCase()),
                                                                    console.log("公钥是："),
                                                                    console.log(this.signatureInfo.appKey),
                                                                    C.setPublicKey(this.signatureInfo.appKey),
                                                                    t.abrupt("return", C.encrypt(a))
                                                            );
                                                        case 13:
                                                        case "end":
                                                            return t.stop();
                                                    }
                                            },
                                            t,
                                            this
                                        );
                                    })
                                );
                                return function () {
                                    return t.apply(this, arguments);
                                };
                            })(),
                        },
                    ]),
                        e
                );
            })(),
            x =
                ((i = void 0),
                    function () {
                        return i || (i = new A()), i;
                    });
        e.a = x;
    }).call(e, n("mtWM"), n("oqQY"));
}