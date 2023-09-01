webpackJsonp(
  [8],
  {
    "/kga": function (t, e, n) {
      "use strict";
      var a = n("JkZY"),
        i =
          (a.a,
          Boolean,
          String,
          String,
          Number,
          String,
          String,
          Boolean,
          Object,
          Boolean,
          {
            mixins: [a.a],
            name: "x-dialog",
            model: { prop: "show", event: "change" },
            props: {
              show: { type: Boolean, default: !1 },
              maskTransition: { type: String, default: "vux-mask" },
              maskZIndex: [String, Number],
              dialogTransition: { type: String, default: "vux-dialog" },
              dialogClass: { type: String, default: "weui-dialog" },
              hideOnBlur: Boolean,
              dialogStyle: Object,
              scroll: {
                type: Boolean,
                default: !0,
                validator: function (t) {
                  return !0;
                },
              },
            },
            computed: {
              maskStyle: function () {
                if (void 0 !== this.maskZIndex)
                  return { zIndex: this.maskZIndex };
              },
            },
            mounted: function () {
              "undefined" != typeof window &&
                window.VUX_CONFIG &&
                "VIEW_BOX" === window.VUX_CONFIG.$layout &&
                (this.layout = "VIEW_BOX");
            },
            watch: {
              show: function (t) {
                this.$emit("update:show", t),
                  this.$emit(t ? "on-show" : "on-hide"),
                  t ? this.addModalClassName() : this.removeModalClassName();
              },
            },
            methods: {
              shouldPreventScroll: function () {
                var t = /iPad|iPhone|iPod/i.test(window.navigator.userAgent),
                  e =
                    this.$el.querySelector("input") ||
                    this.$el.querySelector("textarea");
                if (t && e) return !0;
              },
              hide: function () {
                this.hideOnBlur &&
                  (this.$emit("update:show", !1),
                  this.$emit("change", !1),
                  this.$emit("on-click-mask"));
              },
            },
            data: function () {
              return { layout: "" };
            },
          }),
        r = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "div",
              {
                staticClass: "vux-x-dialog",
                class: { "vux-x-dialog-absolute": "VIEW_BOX" === t.layout },
              },
              [
                n("transition", { attrs: { name: t.maskTransition } }, [
                  n("div", {
                    directives: [
                      {
                        name: "show",
                        rawName: "v-show",
                        value: t.show,
                        expression: "show",
                      },
                    ],
                    staticClass: "weui-mask",
                    style: t.maskStyle,
                    on: { click: t.hide },
                  }),
                ]),
                t._v(" "),
                n("transition", { attrs: { name: t.dialogTransition } }, [
                  n(
                    "div",
                    {
                      directives: [
                        {
                          name: "show",
                          rawName: "v-show",
                          value: t.show,
                          expression: "show",
                        },
                      ],
                      class: t.dialogClass,
                      style: t.dialogStyle,
                    },
                    [t._t("default")],
                    2
                  ),
                ]),
              ],
              1
            );
          },
          staticRenderFns: [],
        };
      var o = n("VU/8")(
        i,
        r,
        !1,
        function (t) {
          n("z3SG");
        },
        null,
        null
      );
      e.a = o.exports;
    },
    "0nrA": function (t, e) {},
    "1ANT": function (t, e, n) {
      "use strict";
      var a = n("mvHQ"),
        i = n.n(a),
        r = n("pFYg"),
        o = n.n(r),
        s = n("Zrlr"),
        u = n.n(s),
        c = n("wxAW"),
        l = n.n(c),
        d = (function () {
          function t(e) {
            u()(this, t), (this.storeObj = window[e] || "");
          }
          return (
            l()(t, [
              {
                key: "set",
                value: function (t, e) {
                  var n = void 0;
                  if (e && "object" === (void 0 === e ? "undefined" : o()(e)))
                    try {
                      n = i()(e);
                    } catch (t) {
                      console.log(t);
                    }
                  else n = e;
                  this.storeObj && this.storeObj.setItem(t, n);
                },
              },
              {
                key: "get",
                value: function (t) {
                  var e = this.storeObj && this.storeObj.getItem(t);
                  if ("undefined" !== e)
                    try {
                      e = JSON.parse(e);
                    } catch (t) {
                      console.log(t);
                    }
                  else e = "";
                  return e;
                },
              },
              {
                key: "del",
                value: function (t) {
                  this.storeObj.removeItem(t);
                },
              },
              {
                key: "clean",
                value: function () {
                  this.storeObj.clear();
                },
              },
            ]),
            t
          );
        })();
      e.a = d;
    },
    "1DHf": function (t, e, n) {
      "use strict";
      var a = n("kbG3"),
        i = n("0FxO"),
        r = n("2IIR"),
        o = n("wmxo"),
        s = n("vLYD"),
        u =
          (a.a,
          Object(r.a)(),
          {
            name: "cell",
            components: { InlineDesc: a.a },
            props: Object(r.a)(),
            created: function () {
              0;
            },
            beforeMount: function () {
              (this.hasTitleSlot = !!this.$slots.title), this.$slots.value;
            },
            computed: {
              labelStyles: function () {
                return Object(o.a)({
                  width: Object(s.a)(this, "labelWidth"),
                  textAlign: Object(s.a)(this, "labelAlign"),
                  marginRight: Object(s.a)(this, "labelMarginRight"),
                });
              },
              valueClass: function () {
                return {
                  "vux-cell-primary":
                    "content" === this.primary || "left" === this.valueAlign,
                  "vux-cell-align-left": "left" === this.valueAlign,
                  "vux-cell-arrow-transition": !!this.arrowDirection,
                  "vux-cell-arrow-up": "up" === this.arrowDirection,
                  "vux-cell-arrow-down": "down" === this.arrowDirection,
                };
              },
              labelClass: function () {
                return {
                  "vux-cell-justify":
                    "justify" === this.$parent.labelAlign ||
                    "justify" === this.$parent.$parent.labelAlign,
                };
              },
              style: function () {
                if (this.alignItems) return { alignItems: this.alignItems };
              },
            },
            methods: {
              onClick: function () {
                !this.disabled && Object(i.a)(this.link, this.$router);
              },
            },
            data: function () {
              return { hasTitleSlot: !0, hasMounted: !1 };
            },
          }),
        c = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "div",
              {
                staticClass: "weui-cell",
                class: {
                  "vux-tap-active": t.isLink || !!t.link,
                  "weui-cell_access": t.isLink || !!t.link,
                  "vux-cell-no-border-intent": !t.borderIntent,
                  "vux-cell-disabled": t.disabled,
                },
                style: t.style,
                on: { click: t.onClick },
              },
              [
                n("div", { staticClass: "weui-cell__hd" }, [t._t("icon")], 2),
                t._v(" "),
                n(
                  "div",
                  {
                    staticClass: "vux-cell-bd",
                    class: {
                      "vux-cell-primary":
                        "title" === t.primary && "left" !== t.valueAlign,
                    },
                  },
                  [
                    n(
                      "p",
                      [
                        t.title || t.hasTitleSlot
                          ? n(
                              "label",
                              {
                                staticClass: "vux-label",
                                class: t.labelClass,
                                style: t.labelStyles,
                              },
                              [t._t("title", [t._v(t._s(t.title))])],
                              2
                            )
                          : t._e(),
                        t._v(" "),
                        t._t("after-title"),
                      ],
                      2
                    ),
                    t._v(" "),
                    n(
                      "inline-desc",
                      [t._t("inline-desc", [t._v(t._s(t.inlineDesc))])],
                      2
                    ),
                  ],
                  1
                ),
                t._v(" "),
                n(
                  "div",
                  { staticClass: "weui-cell__ft", class: t.valueClass },
                  [
                    t._t("value"),
                    t._v(" "),
                    t._t("default", [t._v(t._s(t.value))]),
                    t._v(" "),
                    t.isLoading
                      ? n("i", { staticClass: "weui-loading" })
                      : t._e(),
                  ],
                  2
                ),
                t._v(" "),
                t._t("child"),
              ],
              2
            );
          },
          staticRenderFns: [],
        };
      var l = n("VU/8")(
        u,
        c,
        !1,
        function (t) {
          n("8qHt");
        },
        null,
        null
      );
      e.a = l.exports;
    },
    "3G5C": function (t, e) {
      t.exports = {
        message: { G_MSG: "1月内のデータのみを表示" },
        placeholder: { SEARCH_STA: "Search station.." },
        general: {
          NO_DATA: "Not more data",
          NET_ERR: "Network Error, Fuck u",
          G_LOAD: "Loading..",
          G_LOAD_FAIL: "Sorry,Load failed ",
          U_CNY: "CNY",
          U_COUNT: "1 Count",
          U_N_COUNT: "Count",
          G_TIME_OUT: "Timeout",
          G_MAYBE: "May be?",
          G_QUERY_FAIL: "Sorry query failed,",
        },
        dataPicker: { CANCEL: "Cancel", CONFIRM: "🐮🍺", CLEAR: "Clear" },
        title: {
          TRIP_LS: "My trip",
          TRIP_DE: "TripDetail",
          TRADE_LS: "TradeList",
          TRD_D_RFD: "TradeDetail - Refund",
          TRD_D_RCG: "TradeDetail - Recharge",
          TRD_D_RID: "TradeDetail - Ride",
          TRD_D_CON: "TradeDetail - Consume",
        },
        tripList: {
          TAB_DONE: "Done",
          TAB_TRIP: "Triping",
          PULL_START: "Pull",
          PULL_DONE: "Pull done",
          DONW_REF_START: "Down",
          DONW_REF_DONE: "f@ck u",
          IN_STA_TIME: "InTime",
          OUT_STA_TIME: "OutTime",
          SCAN_TIME: "Scan time",
          FLG_MTR: "Metro - ",
          FLG_BUS: "Bus - ",
          S_TRIP_SUP: "Supplement",
          S_TRIP_PAY: "Now pay",
          S_TRIPING: "Triping",
          S_TRIP_DONE: "Done",
          S_TRIP_NOIN: "Not in",
          S_TRIP_NOOUT: "Not out",
          S_TIME_OUT: "Time out",
        },
        tripDetail: {
          S_TRIPING: "Triping",
          S_UNPAID: "Unpaid",
          S_PAID: "Trip paid",
          S_SUP_SUBMIT: "Supplement submit",
          S_PAY_SUBMIT: "Submission of pay",
          T_OPS_1: "Select you out station",
          T_OPS_2: "Pay for you trip",
          T_OPS_91: "Pay done",
          T_OPS_92: "Pay done",
          B_RIDE_LINE: "BUS Line",
          B_RIDE_STA: "BUS Station",
          REFUND_LINK: "Trip refunded, learn more>>",
          PAID_FAIL_REA: "Paid fail reason:",
          FEEDBACK_BTN: "Feedback",
          T_SELECT_STA: "Plz select station",
          S_HANDING: "Handing",
          S_SUP_DONE: "Supplement submit",
          S_SUP_ERR: "Supplement fial,",
          S_PAY_DONE: "Pay submit",
          S_PAY_ERR: "Pay fial,",
          S_RFD_LK_FAIL: "Sorry,Query fail",
          TRIP_LOAD_ERR: "Trip load fail",
          BTN_SELECT_STA: "Select",
          BTN_RESELECT_STA: "Reselection",
          BTN_SUP_SUBMIT: "Supplement",
          BTN_PAY_SUBMIT: "Pay",
        },
        tradeList: {
          T_RECG_C: "CountRecharge",
          T_RECG_A: "AmountRecharge",
          T_RECG: "Recharge",
          T_RIDE: "Trip",
          T_COMS: "Consume",
          MENU_RIDE: "Trip",
          MENU_NORMAL: "Consume",
          MENU_RECG: "Recharge",
          TYPE_CLASS: "Classify",
          TRD_SUC: "Trade success",
          TRD_FAIL: "Trade fail",
          TRD_RFD: "Trade Refund",
          TRD_RVK: "Trade revoke",
          TRD_CANCEL: "Trade cancel",
          PAY_FAIL: "Paid fail",
          PAYING: "In payment",
          N_RFD: "Refund",
          MONTH: "Month",
          NOW_MONTH: "Current",
        },
        tradeDetail: {
          STATUS: "Status",
          PAY_TIME: "Paytime",
          TRD_STATUS: "TradeStatus",
          TRD_TIME: "TradeTime",
          PAYMENT: "Payment",
          TRADE_ID: "TradeID",
          TRADE_DTL: "Details",
          RFD_TIME: "RefundTime",
          RFD_MENT: "Refundment",
          RFD_ID: "RefundID",
          ORG_ORDER: "OriginOder",
          ACT_PAY: "ActualPay",
          DISCOUNT: "Discount",
          ASS_RFD_ORD: "Associated refund",
          PKL_PAY: "Parkinglot Pay",
          UN_ASS_TRP: "Unknow trip",
          BTN_VIEW: "View",
          T_R_MTR: "Metro",
          T_R_BUS: "Bus",
          T_R_PKL: "Parkinglot",
          T_R_RCG: "Recharge",
          T_D_RFD: "Refund",
        },
        tradeTextMap: {
          SID_101: "Recharge-amount",
          SID_102: "Recharge-count",
          SID_201: "Pay for trip",
          SID_202: "Pay for trip",
          SID_203: "Pay for trip",
          SID_301: "Refund-trip",
          SID_302: "Refund-trip",
          SID_303: "Refund-amount",
          SID_304: "Refund-count",
          SID_305: "Refund-underAmount",
          SID_306: "Refund-trip",
          SID_307: "Refund-Cashier",
          SID_401: "Cashier",
          SID_04: "Parklot",
        },
        orderStatusMap: {
          RECG_SUC: "Recharge success",
          ORDER_CREATE: "Order create",
          ORDER_HANDING: "Order handing",
          TRADE_SUC: "Trade success",
          TRADE_FAIL: "Trade fail",
          ORDER_CLOSE: "Order close",
          PAY_SUC: "Pay success",
          RFD_SUC: "Refund success",
          S_311: "Trade success",
          S_312: "Trade failed",
          S_313: "In payment",
          S_314: "Trade refunde",
          S_315: "Trade revoke",
          S_316: "Trade revoke",
        },
        orderPayModuleMap: {
          ALI_PAY: "AliPay",
          UNION_PAY: "UnionPay",
          AMOUNT: "Amount",
          WECHAT_PAY: "WechatPay",
          COUNT: "count",
          QRCODE_CUS: "Qrcode",
          UNKNOWN: "Unknown",
        },
        refundDescMap: {
          R_301: "Amount consume Refund",
          R_302: "Couting consume Refund",
          R_303: "Amount recharge Refund",
          R_304: "Counting recharge Refund",
          R_305: "Amount Refund",
          R_306: "Trip paid Refund",
          R_307: "Cashier Refund",
          R_311: "Paid success",
          R_312: "Paid fail",
          R_313: "In payment",
          R_314: "Refund",
          R_315: "Trade revoke",
          R_316: "Trade cancel",
        },
        orderDescMap: {
          D_101: "Amount recharge",
          D_102: "Count recharge",
          D_201: "Amount consume",
          D_202: "Counting card consume",
          D_203: "TideCard consume",
          D_204: "QrCode consume",
          D_301: "Refund for Amount",
          D_302: "Refund for Counting card",
          D_303: "Refund for Amount rechanrge",
          D_304: "Refund for Counting card",
          D_305: "Refund for Amount offline",
          D_306: "Refund for TideCard",
        },
        cityMap: {
          CN_3202: "Wuxi",
          CN_3301: "Hangzhou",
          CN_6401: "Yinchuan",
          CN_12: "Tianjin",
          CN_5101: "Chengdu",
          CN_3502: "Xiamen",
          CN_4113: "Nanyang",
          CN_3404: "Huainan",
          CN_4501: "Nanning",
          CN_4107: "Xinxiang",
          CN_350782: "Wuyishan",
          CN_2102: "Dalian",
          CN_5301: "Kunming",
          CN_3601: "Nanchang",
          CN_3100: "Shanghai",
          CN_3302: "Ningbo",
          CN_3201: "Nanjing",
          CN_NAGOYA: "Nagoya",
          CN_HK: "Hongkong",
          CN_SGA: "Singapore",
        },
        weeks: {
          MON: "Monday",
          TUE: "Tuesday",
          WED: "Wednesday",
          THU: "Thursday",
          FRI: "Friday",
          SAT: "Saturday",
          SUN: "Sunday",
        },
      };
    },
    "62KO": function (t, e, n) {
      "use strict";
      var a = n("/kga"),
        i =
          (a.a,
          Boolean,
          Boolean,
          String,
          String,
          Boolean,
          String,
          String,
          String,
          String,
          Number,
          String,
          String,
          String,
          Boolean,
          Object,
          Boolean,
          String,
          Boolean,
          Boolean,
          {
            name: "confirm",
            components: { XDialog: a.a },
            props: {
              value: { type: Boolean, default: !1 },
              showInput: { type: Boolean, default: !1 },
              placeholder: { type: String, default: "" },
              theme: { type: String, default: "ios" },
              hideOnBlur: { type: Boolean, default: !1 },
              title: String,
              confirmText: String,
              cancelText: String,
              maskTransition: { type: String, default: "vux-fade" },
              maskZIndex: [Number, String],
              dialogTransition: { type: String, default: "vux-dialog" },
              content: String,
              closeOnConfirm: { type: Boolean, default: !0 },
              inputAttrs: Object,
              showContent: { type: Boolean, default: !0 },
              confirmType: { type: String, default: "primary" },
              showCancelButton: { type: Boolean, default: !0 },
              showConfirmButton: { type: Boolean, default: !0 },
            },
            created: function () {
              (this.showValue = this.show),
                this.value && (this.showValue = this.value);
            },
            watch: {
              value: function (t) {
                this.showValue = t;
              },
              showValue: function (t) {
                var e = this;
                this.$emit("input", t),
                  t &&
                    (this.showInput &&
                      ((this.msg = ""),
                      setTimeout(function () {
                        e.$refs.input && e.setInputFocus();
                      }, 300)),
                    this.$emit("on-show"));
              },
            },
            data: function () {
              return { msg: "", showValue: !1 };
            },
            methods: {
              getInputAttrs: function () {
                return this.inputAttrs || { type: "text" };
              },
              setInputValue: function (t) {
                this.msg = t;
              },
              setInputFocus: function (t) {
                t && t.preventDefault(), this.$refs.input.focus();
              },
              _onConfirm: function () {
                this.showValue &&
                  (this.closeOnConfirm && (this.showValue = !1),
                  this.$emit("on-confirm", this.msg));
              },
              _onCancel: function () {
                this.showValue &&
                  ((this.showValue = !1), this.$emit("on-cancel"));
              },
            },
          }),
        r = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "div",
              { staticClass: "vux-confirm" },
              [
                n(
                  "x-dialog",
                  {
                    attrs: {
                      "dialog-class":
                        "android" === t.theme
                          ? "weui-dialog weui-skin_android"
                          : "weui-dialog",
                      "mask-transition": t.maskTransition,
                      "dialog-transition":
                        "android" === t.theme ? "vux-fade" : t.dialogTransition,
                      "hide-on-blur": t.hideOnBlur,
                      "mask-z-index": t.maskZIndex,
                    },
                    on: {
                      "on-hide": function (e) {
                        t.$emit("on-hide");
                      },
                    },
                    model: {
                      value: t.showValue,
                      callback: function (e) {
                        t.showValue = e;
                      },
                      expression: "showValue",
                    },
                  },
                  [
                    t.title
                      ? n(
                          "div",
                          {
                            staticClass: "weui-dialog__hd",
                            class: { "with-no-content": !t.showContent },
                          },
                          [
                            n("strong", { staticClass: "weui-dialog__title" }, [
                              t._v(t._s(t.title)),
                            ]),
                          ]
                        )
                      : t._e(),
                    t._v(" "),
                    t.showContent
                      ? [
                          t.showInput
                            ? n("div", { staticClass: "vux-prompt" }, [
                                "checkbox" === t.getInputAttrs().type
                                  ? n(
                                      "input",
                                      t._b(
                                        {
                                          directives: [
                                            {
                                              name: "model",
                                              rawName: "v-model",
                                              value: t.msg,
                                              expression: "msg",
                                            },
                                          ],
                                          ref: "input",
                                          staticClass: "vux-prompt-msgbox",
                                          attrs: {
                                            placeholder: t.placeholder,
                                            type: "checkbox",
                                          },
                                          domProps: {
                                            checked: Array.isArray(t.msg)
                                              ? t._i(t.msg, null) > -1
                                              : t.msg,
                                          },
                                          on: {
                                            touchend: t.setInputFocus,
                                            change: function (e) {
                                              var n = t.msg,
                                                a = e.target,
                                                i = !!a.checked;
                                              if (Array.isArray(n)) {
                                                var r = t._i(n, null);
                                                a.checked
                                                  ? r < 0 &&
                                                    (t.msg = n.concat([null]))
                                                  : r > -1 &&
                                                    (t.msg = n
                                                      .slice(0, r)
                                                      .concat(n.slice(r + 1)));
                                              } else t.msg = i;
                                            },
                                          },
                                        },
                                        "input",
                                        t.getInputAttrs(),
                                        !1
                                      )
                                    )
                                  : "radio" === t.getInputAttrs().type
                                  ? n(
                                      "input",
                                      t._b(
                                        {
                                          directives: [
                                            {
                                              name: "model",
                                              rawName: "v-model",
                                              value: t.msg,
                                              expression: "msg",
                                            },
                                          ],
                                          ref: "input",
                                          staticClass: "vux-prompt-msgbox",
                                          attrs: {
                                            placeholder: t.placeholder,
                                            type: "radio",
                                          },
                                          domProps: {
                                            checked: t._q(t.msg, null),
                                          },
                                          on: {
                                            touchend: t.setInputFocus,
                                            change: function (e) {
                                              t.msg = null;
                                            },
                                          },
                                        },
                                        "input",
                                        t.getInputAttrs(),
                                        !1
                                      )
                                    )
                                  : n(
                                      "input",
                                      t._b(
                                        {
                                          directives: [
                                            {
                                              name: "model",
                                              rawName: "v-model",
                                              value: t.msg,
                                              expression: "msg",
                                            },
                                          ],
                                          ref: "input",
                                          staticClass: "vux-prompt-msgbox",
                                          attrs: {
                                            placeholder: t.placeholder,
                                            type: t.getInputAttrs().type,
                                          },
                                          domProps: { value: t.msg },
                                          on: {
                                            touchend: t.setInputFocus,
                                            input: function (e) {
                                              e.target.composing ||
                                                (t.msg = e.target.value);
                                            },
                                          },
                                        },
                                        "input",
                                        t.getInputAttrs(),
                                        !1
                                      )
                                    ),
                              ])
                            : n(
                                "div",
                                { staticClass: "weui-dialog__bd" },
                                [
                                  t._t("default", [
                                    n("div", {
                                      domProps: { innerHTML: t._s(t.content) },
                                    }),
                                  ]),
                                ],
                                2
                              ),
                        ]
                      : t._e(),
                    t._v(" "),
                    n("div", { staticClass: "weui-dialog__ft" }, [
                      t.showCancelButton
                        ? n(
                            "a",
                            {
                              staticClass:
                                "weui-dialog__btn weui-dialog__btn_default",
                              attrs: { href: "javascript:;" },
                              on: { click: t._onCancel },
                            },
                            [t._v(t._s(t.cancelText || "取消"))]
                          )
                        : t._e(),
                      t._v(" "),
                      t.showConfirmButton
                        ? n(
                            "a",
                            {
                              staticClass: "weui-dialog__btn",
                              class: "weui-dialog__btn_" + t.confirmType,
                              attrs: { href: "javascript:;" },
                              on: { click: t._onConfirm },
                            },
                            [t._v(t._s(t.confirmText || "确定"))]
                          )
                        : t._e(),
                    ]),
                  ],
                  2
                ),
              ],
              1
            );
          },
          staticRenderFns: [],
        };
      var o = n("VU/8")(
        i,
        r,
        !1,
        function (t) {
          n("P1tG");
        },
        null,
        null
      );
      e.a = o.exports;
    },
    "8qHt": function (t, e) {},
    Au3d: function (t, e, n) {
      "use strict";
      (function (t) {
        var a,
          i = n("Xxa5"),
          r = n.n(i),
          o = n("exGp"),
          s = n.n(o),
          u = n("Dd8w"),
          c = n.n(u),
          l = n("Zrlr"),
          d = n.n(l),
          p = n("wxAW"),
          f = n.n(p),
          _ = n("BUAs"),
          h = n.n(_),
          m = n("yCNF"),
          g = n.n(m),
          v = n("IOyA"),
          S = new (n("DRZg").a)("ajax"),
          T = new v.a(),
          y = (function () {
            function e() {
              d()(this, e);
            }
            return (
              f()(e, [
                {
                  key: "loginHandle",
                  value: function (t) {
                    "0005" === t.errcode && T.reLogin();
                  },
                },
                {
                  key: "handlRes",
                  value: function (t) {
                    var e = { isSuc: !1, data: {} },
                      n = t.status,
                      a = t.data,
                      i = t.statusText;
                    if (200 !== n)
                      return (
                        console.error(
                          "server err.status is " +
                            n +
                            "\n            statusText is " +
                            i
                        ),
                        { isSuc: !1, msg: i || "服务端错误" }
                      );
                    (e = c()({}, a)), this.loginHandle(e);
                    var r = a.errcode,
                      o = a.errmsg,
                      s = a.result;
                    return "0000" !== r
                      ? ((e.isSuc = !1), (e.msg = o), (e.errCode = r), e)
                      : ((e.msg = o),
                        (e.isSuc = !0),
                        (e.info = s),
                        (e.errCode = r),
                        e);
                  },
                },
                {
                  key: "post",
                  value: (function () {
                    var e = s()(
                      r.a.mark(function e(n, a, i) {
                        var o, s;
                        return r.a.wrap(
                          function (e) {
                            for (;;)
                              switch ((e.prev = e.next)) {
                                case 0:
                                  return (e.next = 2), T.getConfig(n, a);
                                case 2:
                                  return (
                                    (o = e.sent),
                                    g()(i) &&
                                      ((o.headers = h()(o.headers, i)),
                                      delete o.headers.app_aplication_type),
                                    (s = void 0),
                                    console.log(o),
                                    (e.prev = 6),
                                    (e.next = 9),
                                    t(o)
                                  );
                                case 9:
                                  (s = e.sent), (e.next = 18);
                                  break;
                                case 12:
                                  return (
                                    (e.prev = 12),
                                    (e.t0 = e.catch(6)),
                                    console.log(e.t0),
                                    S.log(e.t0 && e.t0.message),
                                    console.error(e.t0),
                                    e.abrupt("return")
                                  );
                                case 18:
                                  return e.abrupt("return", this.handlRes(s));
                                case 19:
                                case "end":
                                  return e.stop();
                              }
                          },
                          e,
                          this,
                          [[6, 12]]
                        );
                      })
                    );
                    return function (t, n, a) {
                      return e.apply(this, arguments);
                    };
                  })(),
                },
              ]),
              e
            );
          })(),
          R =
            ((a = void 0),
            function () {
              return a || (a = new y()), a;
            });
        e.a = R;
      }).call(e, n("mtWM"));
    },
    Bfwr: function (t, e, n) {
      "use strict";
      Boolean, String, String, String;
      var a = {
          name: "loading",
          model: { prop: "show", event: "change" },
          props: {
            show: Boolean,
            text: String,
            position: String,
            transition: { type: String, default: "vux-mask" },
          },
          watch: {
            show: function (t) {
              this.$emit("update:show", t);
            },
          },
        },
        i = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n("transition", { attrs: { name: t.transition } }, [
              n(
                "div",
                {
                  directives: [
                    {
                      name: "show",
                      rawName: "v-show",
                      value: t.show,
                      expression: "show",
                    },
                  ],
                  staticClass: "weui-loading_toast vux-loading",
                  class: t.text ? "" : "vux-loading-no-text",
                },
                [
                  n("div", { staticClass: "weui-mask_transparent" }),
                  t._v(" "),
                  n(
                    "div",
                    {
                      staticClass: "weui-toast",
                      style: { position: t.position },
                    },
                    [
                      n("i", { staticClass: "weui-loading weui-icon_toast" }),
                      t._v(" "),
                      t.text
                        ? n(
                            "p",
                            { staticClass: "weui-toast__content" },
                            [t._v(t._s(t.text || "加载中")), t._t("default")],
                            2
                          )
                        : t._e(),
                    ]
                  ),
                ]
              ),
            ]);
          },
          staticRenderFns: [],
        };
      var r = n("VU/8")(
        a,
        i,
        !1,
        function (t) {
          n("QaG2");
        },
        null,
        null
      );
      e.a = r.exports;
    },
    D1y7: function (t, e, n) {
      "use strict";
      var a = n("Av7u"),
        i = n.n(a);
      e.a = {
        decrypt: function (t) {
          var e = sessionStorage.getItem("keyRandom") || "1234567890123456",
            n = i.a.enc.Utf8.parse(e),
            a = i.a.enc.Utf8.parse(t),
            r = i.a.enc.Utf8.stringify(a),
            o = i.a.AES.decrypt(r, n, {
              mode: i.a.mode.ECB,
              padding: i.a.pad.Pkcs7,
            });
          return o.toString(i.a.enc.Utf8).toString();
        },
        encrypt: function (t) {
          var e = sessionStorage.getItem("keyRandom") || "1234567890123456",
            n = i.a.enc.Utf8.parse(e);
          return i.a.AES.encrypt(t, n, {
            mode: i.a.mode.ECB,
            padding: i.a.pad.Pkcs7,
          })
            .ciphertext.toString()
            .toUpperCase();
        },
        setKey: function () {
          var t = Math.floor(Math.random() * (9e15 + 1) + 1e15) + "";
          sessionStorage.setItem("keyRandom", t);
        },
      };
    },
    DRZg: function (t, e, n) {
      "use strict";
      var a = n("mvHQ"),
        i = n.n(a),
        r = n("pFYg"),
        o = n.n(r),
        s = n("Zrlr"),
        u = n.n(s),
        c = n("wxAW"),
        l = n.n(c),
        d = n("oMTx"),
        p = (function () {
          function t(e) {
            u()(this, t), (this.module = e);
          }
          return (
            l()(t, [
              {
                key: "getStanOut",
                value: function (t) {
                  var e =
                    arguments.length > 1 && void 0 !== arguments[1]
                      ? arguments[1]
                      : "";
                  if (t && "object" === (void 0 === t ? "undefined" : o()(t)))
                    try {
                      t = i()(t);
                    } catch (t) {
                      console.log(t);
                    }
                  return [this.module, e, t].join(" ");
                },
              },
              {
                key: "saveLogToNative",
                value: function (t, e) {
                  d.a.util.logFile({
                    level: t,
                    msg: e,
                    success: function (t) {
                      console.log(i()(t));
                    },
                    error: function (t) {
                      console.log("失败:" + i()(t));
                    },
                  });
                },
              },
              {
                key: "factoryHandle",
                value: function (t, e) {
                  var n =
                    arguments.length > 2 && void 0 !== arguments[2]
                      ? arguments[2]
                      : "";
                  window &&
                    window.eruda &&
                    console &&
                    console[t] &&
                    console[t](e);
                  var a = this.getStanOut(e, n);
                  this.saveLogToNative(t, a);
                },
              },
              {
                key: "log",
                value: function (t, e) {
                  this.factoryHandle("log", t, e);
                },
              },
              {
                key: "info",
                value: function (t, e) {
                  this.factoryHandle("info", t, e);
                },
              },
              {
                key: "error",
                value: function (t, e) {
                  this.factoryHandle("error", t, e);
                },
              },
              {
                key: "warn",
                value: function (t, e) {
                  this.factoryHandle("warn", t, e);
                },
              },
            ]),
            t
          );
        })();
      e.a = p;
    },
    IOyA: function (t, e, n) {
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
                            for (;;)
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
                      error: function (t) {},
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
                              params: { title: "", pageUrl: "" },
                              success: function (t) {},
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
                            for (;;)
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
                            for (;;)
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
                            for (;;)
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
                            for (;;)
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
                                  (e.t1 = { data: a }), (e.next = 15);
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
                                    (n = o()({ bundleId: s }, c, {
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
                            for (;;)
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
    },
    IuJc: function (t, e) {
      t.exports = {
        dev: { appId: "c81e728d9d4c2f636f067f89cc14862c", baseUrl: "" },
      };
    },
    Js7q: function (t, e) {},
    NHnr: function (t, e, n) {
      "use strict";
      Object.defineProperty(e, "__esModule", { value: !0 });
      var a = n("Xxa5"),
        i = n.n(a),
        r = n("exGp"),
        o = n.n(r),
        s = n("mvHQ"),
        u = n.n(s),
        c = n("7+uW"),
        l = {
          render: function () {
            var t = this.$createElement,
              e = this._self._c || t;
            return e(
              "div",
              { attrs: { id: "app" } },
              [e("router-view", { staticClass: "view app-view" })],
              1
            );
          },
          staticRenderFns: [],
        };
      var d = n("VU/8")(
          {
            name: "App",
            data: function () {
              return { transitionName: "fold-left" };
            },
            beforeCreate: function () {},
            watch: {},
          },
          l,
          !1,
          function (t) {
            n("ZqI+"), n("NwWW");
          },
          null,
          null
        ).exports,
        p = n("Utns"),
        f = n.n(p),
        _ = n("/ocq"),
        h = function () {
          return n
            .e(3)
            .then(n.bind(null, "PxjV"))
            .then(function (t) {
              return t.default;
            });
        },
        m = function () {
          return n
            .e(2)
            .then(n.bind(null, "RkJB"))
            .then(function (t) {
              return t.default;
            });
        },
        g = function () {
          return n
            .e(5)
            .then(n.bind(null, "oaTu"))
            .then(function (t) {
              return t.default;
            });
        },
        v = function () {
          return n
            .e(0)
            .then(n.bind(null, "/37X"))
            .then(function (t) {
              return t.default;
            });
        },
        S = function () {
          return n
            .e(1)
            .then(n.bind(null, "zQA/"))
            .then(function (t) {
              return t.default;
            });
        },
        T = function () {
          return n
            .e(4)
            .then(n.bind(null, "OV2r"))
            .then(function (t) {
              return t.default;
            });
        };
      c.a.use(_.a);
      var y = "";
      var R = {
          routes: [
            {
              path: "/",
              name: "Home",
              component: function () {
                return n
                  .e(6)
                  .then(n.bind(null, "ISHt"))
                  .then(function (t) {
                    return t.default;
                  });
              },
              mate: { title: "hello world " + y },
            },
            { path: "/testPage", name: T, component: T },
            { path: "/appointmentList", name: h, component: h },
            { path: "/appointmentRecordList", name: m, component: m },
            { path: "/appointmentMain", name: g, component: g },
            { path: "/appointmentRecordDetail", name: v, component: v },
            { path: "/travelCard", name: S, component: S },
          ],
        },
        w = new _.a(R),
        C = n("NYxO"),
        D = {
          state: { token: {} },
          getters: { getUser: function (t, e) {}, getToken: function () {} },
          actions: {
            registerToken: function (t, e) {
              var n = this;
              t.commit;
              return o()(
                i.a.mark(function t() {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    n
                  );
                })
              )();
            },
            removeToken: function (t) {
              var e = this;
              t.commit, t.getters;
              return o()(
                i.a.mark(function t() {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    e
                  );
                })
              )();
            },
          },
          mutations: {
            REGISTER_TOKEN: function (t, e) {},
            REMOVE_TOKEN: function (t) {},
          },
        };
      c.a.use(C.a);
      var A = new C.a.Store({ modules: { token: D } }),
        x = n("Dd8w"),
        I = n.n(x),
        N = n("BUAs"),
        b = n.n(N),
        k = n("9uKM"),
        E = n.n(k),
        P = n("kbi+"),
        O = n.n(P),
        U = n("RyI1"),
        M = n.n(U),
        L = n("2247"),
        B = n.n(L),
        F = n("Au3d"),
        H = n("IOyA"),
        V = n("IuJc"),
        $ = n("1ANT"),
        G = n("oMTx"),
        Y = n("DRZg");
      G.a.error(function (t) {
        console.log("错误:" + u()(t));
      }),
        G.a.config(),
        G.a.ready(function () {
          console.log("注册成功");
        });
      var j = { map: B.a, filter: M.a, find: O.a, each: E.a, assign: b.a },
        K = {};
      (K.network = new H.a()),
        (K._ = j),
        (K.config = V),
        (K.ajax = new F.a()),
        (K.localCache = new $.a("localStorage")),
        (K.sessionCache = new $.a("sessionStorage")),
        (K.bwtHybrid = G.a),
        (K.logger = Y.a);
      var W,
        q = K,
        Q = q.ajax,
        z = { version: "0100" },
        X = {
          mgApi: {
            getLines: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/dict/v1/query-lines",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            supportStationList: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/console/appoint/supportStationList",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            appiontSubmit: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/appiont/submit",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            getAppiontTimeList: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/appiont/list",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            queryAppiontList: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/in-station/queryOrderList",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            queryAppiontDetail: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/in-station/queryOrderInfo",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            queryCard: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post("/bas/ncp/v1/card/query", e, I()({}, z, n))
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            addCard: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post("/bas/ncp/v1/card/bind", e, I()({}, z, n))
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            updateCardInfo: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/card/update",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
            queryAppiontCancel: (function () {
              var t = o()(
                i.a.mark(function t(e, n) {
                  return i.a.wrap(
                    function (t) {
                      for (;;)
                        switch ((t.prev = t.next)) {
                          case 0:
                            return (
                              (t.next = 2),
                              Q.post(
                                "/bas/ncp/v1/appiont/cancel",
                                e,
                                I()({}, z, n)
                              )
                            );
                          case 2:
                            return t.abrupt("return", t.sent);
                          case 3:
                          case "end":
                            return t.stop();
                        }
                    },
                    t,
                    this
                  );
                })
              );
              return function (e, n) {
                return t.apply(this, arguments);
              };
            })(),
          },
        },
        Z = n("rHil"),
        J = n("1DHf"),
        tt = n("TXmL"),
        et = n("NXWw"),
        nt = n("3BeM"),
        at = n("Y+qm"),
        it = n("oVYx"),
        rt = n("Peep"),
        ot = n("POcy"),
        st = n.n(ot),
        ut = n("aCbg"),
        ct = n.n(ut),
        lt = n("D1y7"),
        dt = this;
      c.a.use(function (t) {
        t.component("group", Z.a),
          t.component("cell", J.a),
          Object.defineProperty(t.prototype, "$api", { value: X }),
          Object.defineProperty(t.prototype, "$bwtHybrid", {
            value: q.bwtHybrid,
          }),
          Object.defineProperty(t.prototype, "$_", { value: q._ }),
          Object.defineProperty(t.prototype, "$network", { value: q.network }),
          Object.defineProperty(t.prototype, "$networkV2", {
            value: q.networkV2,
          }),
          Object.defineProperty(t.prototype, "$config", { value: q.config }),
          Object.defineProperty(t.prototype, "$localCache", {
            value: q.localCache,
          }),
          Object.defineProperty(t.prototype, "$sessionCache", {
            value: q.sessionCache,
          });
      }),
        c.a.use(tt.a),
        c.a.component(ct.a.name, ct.a),
        c.a.use(st.a),
        c.a.use(et.a),
        c.a.use(nt.a),
        c.a.use(at.a),
        c.a.use(it.a),
        c.a.use(rt.a),
        (c.a.config.productionTip = !1),
        G.a.error(function (t) {
          console.log("错误2:" + u()(t));
        }),
        G.a.config(),
        G.a.ready(function () {
          console.log("注册成功");
        }),
        w.beforeEach(
          ((W = o()(
            i.a.mark(function t(e, n, a) {
              return i.a.wrap(
                function (t) {
                  for (;;)
                    switch ((t.prev = t.next)) {
                      case 0:
                        a();
                      case 1:
                      case "end":
                        return t.stop();
                    }
                },
                t,
                dt
              );
            })
          )),
          function (t, e, n) {
            return W.apply(this, arguments);
          })
        ),
        w.afterEach(function (t, e) {});
      var pt = navigator.userAgent,
        ft = pt.indexOf("Android");
      ft >= 0 && parseFloat(pt.slice(ft + 8)) < 4.5 && n("hKoQ").polyfill();
      var _t,
        ht =
          "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 i18n/en-US";
      (_t =
        ht.indexOf("i18n") > -1
          ? ht.substr(ht.indexOf("i18n") + 5, ht.indexOf("i18n") + 10)
          : "en-US"),
        lt.a.setKey(),
        window.localStorage.setItem("isTimeLoop", "done");
      var mt = new tt.a({
        locale: _t,
        messages: { "zh-CN": n("kpEQ"), "en-US": n("3G5C") },
      });
      f.a.attach(document.body),
        (window.vm = new c.a({
          el: "#app-box",
          i18n: mt,
          router: w,
          store: A,
          render: function (t) {
            return t(d);
          },
        })),
        console.log("H5进出站预约 Ver 1.0.0 build141350"),
        (window.alert = function (t) {
          var e = document.createElement("IFRAME");
          (e.style.display = "none"),
            e.setAttribute("src", "data:text/plain,"),
            document.documentElement.appendChild(e),
            window.frames[0].window.alert(t),
            e.parentNode.removeChild(e);
        });
    },
    NnOP: function (t, e) {},
    NwWW: function (t, e) {},
    P1tG: function (t, e) {},
    QaG2: function (t, e) {},
    UNGY: function (t, e, n) {
      "use strict";
      var a = n("fZjL"),
        i = n.n(a),
        r =
          (String,
          Boolean,
          {
            name: "icon",
            props: { type: String, isMsg: Boolean },
            computed: {
              className: function () {
                return (
                  "weui-icon weui_icon_" +
                  this.type +
                  " weui-icon-" +
                  this.type.replace(/_/g, "-")
                );
              },
            },
          }),
        o = {
          render: function () {
            var t = this.$createElement;
            return (this._self._c || t)("i", {
              class: [this.className, this.isMsg ? "weui-icon_msg" : ""],
            });
          },
          staticRenderFns: [],
        };
      var s = n("VU/8")(
          r,
          o,
          !1,
          function (t) {
            n("qKOS");
          },
          null,
          null
        ).exports,
        u = n("zV4+"),
        c = n("rHil"),
        l = n("kbG3"),
        d = n("KRg4"),
        p = n("ODCk"),
        f =
          (d.a,
          c.a,
          l.a,
          String,
          String,
          String,
          String,
          String,
          Number,
          Number,
          String,
          String,
          String,
          String,
          String,
          String,
          String,
          String,
          Boolean,
          Number,
          Number,
          String,
          String,
          String,
          Function,
          Boolean,
          Array,
          Array,
          Boolean,
          String,
          Function,
          Function,
          Object,
          {
            name: "datetime",
            mixins: [d.a],
            components: { Group: c.a, InlineDesc: l.a, Icon: s },
            props: {
              format: {
                type: String,
                default: "YYYY-MM-DD",
                validator: function (t) {
                  return !0;
                },
              },
              title: String,
              value: { type: String, default: "" },
              inlineDesc: String,
              placeholder: String,
              minYear: Number,
              maxYear: Number,
              confirmText: String,
              cancelText: String,
              clearText: String,
              yearRow: { type: String, default: "{value}" },
              monthRow: { type: String, default: "{value}" },
              dayRow: { type: String, default: "{value}" },
              hourRow: { type: String, default: "{value}" },
              minuteRow: { type: String, default: "{value}" },
              required: { type: Boolean, default: !1 },
              minHour: { type: Number, default: 0 },
              maxHour: { type: Number, default: 23 },
              startDate: {
                type: String,
                validator: function (t) {
                  return !t || 10 === t.length;
                },
              },
              endDate: {
                type: String,
                validator: function (t) {
                  return !t || 10 === t.length;
                },
              },
              valueTextAlign: String,
              displayFormat: Function,
              readonly: Boolean,
              hourList: Array,
              minuteList: Array,
              show: Boolean,
              defaultSelectedValue: String,
              computeHoursFunction: Function,
              computeDaysFunction: Function,
              orderMap: Object,
            },
            created: function () {
              (this.isFirstSetValue = !1), (this.currentValue = this.value);
            },
            data: function () {
              return {
                currentShow: !1,
                currentValue: null,
                valid: !0,
                errors: {},
              };
            },
            mounted: function () {
              var t = this,
                e = this.uuid;
              this.$el.setAttribute("id", "vux-datetime-" + e),
                this.readonly ||
                  this.$nextTick(function () {
                    t.render(),
                      t.show &&
                        t.$nextTick(function () {
                          t.picker && t.picker.show(t.currentValue);
                        });
                  });
            },
            computed: {
              styles: function () {
                return this.$parent
                  ? {
                      width: this.$parent.labelWidth,
                      textAlign: this.$parent.labelAlign,
                      marginRight: this.$parent.labelMarginRight,
                    }
                  : {};
              },
              pickerOptions: function () {
                var t = this,
                  e = {
                    trigger: "#vux-datetime-" + this.uuid,
                    format: this.format,
                    value: this.currentValue,
                    output: ".vux-datetime-value",
                    confirmText: t.getButtonText("confirm"),
                    cancelText: t.getButtonText("cancel"),
                    clearText: t.clearText,
                    yearRow: this.yearRow,
                    monthRow: this.monthRow,
                    dayRow: this.dayRow,
                    hourRow: this.hourRow,
                    minuteRow: this.minuteRow,
                    minHour: this.minHour,
                    maxHour: this.maxHour,
                    startDate: this.startDate,
                    endDate: this.endDate,
                    hourList: this.hourList,
                    minuteList: this.minuteList,
                    defaultSelectedValue: this.defaultSelectedValue,
                    computeHoursFunction: this.computeHoursFunction,
                    computeDaysFunction: this.computeDaysFunction,
                    orderMap: this.orderMap || {},
                    onSelect: function (e, n, a) {
                      t.picker &&
                        t.picker.config.renderInline &&
                        (t.$emit("input", a), t.$emit("on-change", a));
                    },
                    onConfirm: function (e) {
                      t.currentValue = e;
                    },
                    onClear: function (e) {
                      t.$emit("on-clear", e);
                    },
                    onHide: function (e) {
                      (t.currentShow = !1),
                        t.$emit("update:show", !1),
                        t.validate(),
                        t.$emit("on-hide", e),
                        "cancel" === e && t.$emit("on-cancel"),
                        "confirm" === e &&
                          setTimeout(function () {
                            t.$nextTick(function () {
                              t.$emit("on-confirm", t.value);
                            });
                          });
                    },
                    onShow: function () {
                      (t.currentShow = !0),
                        t.$emit("update:show", !0),
                        t.$emit("on-show");
                    },
                  };
                return (
                  this.minYear && (e.minYear = this.minYear),
                  this.maxYear && (e.maxYear = this.maxYear),
                  e
                );
              },
              firstError: function () {
                var t = i()(this.errors)[0];
                return this.errors[t];
              },
              labelClass: function () {
                return this.$parent
                  ? {
                      "vux-cell-justify":
                        "justify" === this.$parent.labelAlign ||
                        "justify" === this.$parent.$parent.labelAlign,
                    }
                  : {};
              },
            },
            methods: {
              getButtonText: function (t) {
                return "cancel" === t && this.cancelText
                  ? this.cancelText
                  : "confirm" === t && this.confirmText
                  ? this.confirmText
                  : this.$el.getAttribute("data-" + t + "-text");
              },
              render: function () {
                var t = this;
                this.$nextTick(function () {
                  t.picker && t.picker.destroy(),
                    (t.picker = new u.a(t.pickerOptions));
                });
              },
              validate: function () {
                if (!this.currentValue && this.required)
                  return (
                    (this.valid = !1), void (this.errors.required = "必填")
                  );
                (this.valid = !0), (this.errors = {});
              },
            },
            watch: {
              readonly: function (t) {
                t ? this.picker && this.picker.destroy() : this.render();
              },
              show: function (t) {
                t !== this.currentShow &&
                  (t
                    ? this.picker && this.picker.show(this.currentValue)
                    : this.picker && this.picker.hide(this.currentValue));
              },
              currentValue: function (t, e) {
                this.$emit("input", t),
                  this.isFirstSetValue
                    ? this.$emit("on-change", t)
                    : ((this.isFirstSetValue = !0),
                      e && this.$emit("on-change", t)),
                  this.validate();
              },
              startDate: function () {
                this.render();
              },
              endDate: function () {
                this.render();
              },
              format: function (t) {
                this.currentValue &&
                  (this.currentValue = Object(p.a)(this.currentValue, t)),
                  this.render();
              },
              value: function (t) {
                this.readonly ||
                (this.picker && this.picker.config.renderInline)
                  ? (this.currentValue = t)
                  : this.currentValue !== t &&
                    ((this.currentValue = t), this.render());
              },
            },
            beforeDestroy: function () {
              this.picker && this.picker.destroy();
            },
          }),
        _ = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "a",
              {
                staticClass: "vux-datetime weui-cell",
                class: { "weui-cell_access": !t.readonly },
                attrs: {
                  "data-cancel-text": "取消",
                  "data-confirm-text": "确定",
                  href: "javascript:",
                },
              },
              [
                t._t("default", [
                  n(
                    "div",
                    [
                      t._t("title", [
                        n("p", {
                          class: t.labelClass,
                          style: t.styles,
                          domProps: { innerHTML: t._s(t.title) },
                        }),
                      ]),
                      t._v(" "),
                      t.inlineDesc
                        ? n("inline-desc", [t._v(t._s(t.inlineDesc))])
                        : t._e(),
                    ],
                    2
                  ),
                  t._v(" "),
                  n(
                    "div",
                    {
                      staticClass:
                        "weui-cell__ft vux-cell-primary vux-datetime-value",
                      style: { textAlign: t.valueTextAlign },
                    },
                    [
                      !t.currentValue && t.placeholder
                        ? n("span", { staticClass: "vux-cell-placeholder" }, [
                            t._v(t._s(t.placeholder)),
                          ])
                        : t._e(),
                      t._v(" "),
                      t.currentValue
                        ? n("span", { staticClass: "vux-cell-value" }, [
                            t._v(
                              t._s(
                                t.displayFormat
                                  ? t.displayFormat(t.currentValue)
                                  : t.currentValue
                              )
                            ),
                          ])
                        : t._e(),
                      t._v(" "),
                      n("icon", {
                        directives: [
                          {
                            name: "show",
                            rawName: "v-show",
                            value: !t.valid,
                            expression: "!valid",
                          },
                        ],
                        staticClass: "vux-input-icon",
                        attrs: { type: "warn", title: t.firstError },
                      }),
                    ],
                    1
                  ),
                ]),
              ],
              2
            );
          },
          staticRenderFns: [],
        };
      var h = n("VU/8")(
        f,
        _,
        !1,
        function (t) {
          n("NnOP");
        },
        null,
        null
      );
      e.a = h.exports;
    },
    "ZqI+": function (t, e) {},
    kbG3: function (t, e, n) {
      "use strict";
      var a = {
        render: function () {
          var t = this.$createElement;
          return (this._self._c || t)(
            "span",
            { staticClass: "vux-label-desc" },
            [this._t("default")],
            2
          );
        },
        staticRenderFns: [],
      };
      var i = n("VU/8")(
        { name: "inline-desc" },
        a,
        !1,
        function (t) {
          n("Js7q");
        },
        null,
        null
      );
      e.a = i.exports;
    },
    kp3f: function (t, e) {},
    kpEQ: function (t, e) {
      t.exports = {
        message: { G_MSG: "1月内のデータのみを表示" },
        placeholder: { SEARCH_STA: "检索站点.." },
        general: {
          NO_DATA: "没有更多数据",
          NET_ERR: "网络错误，请检查您的网络设置",
          G_LOAD: "努力加载中..",
          G_LOAD_FAIL: "抱歉，加载失败",
          U_CNY: "元",
          U_COUNT: "1 次",
          U_N_COUNT: "次",
          G_TIME_OUT: "超时",
          G_MAYBE: "猜您要选",
          G_QUERY_FAIL: "抱歉，查询失败,",
        },
        dataPicker: { CANCEL: "取消", CONFIRM: "🐮🍺", CLEAR: "清除" },
        title: {
          TRIP_LS: "我的行程",
          TRIP_DE: "行程详情",
          TRADE_LS: "交易明细",
          TRD_D_RFD: "订单详情 - 退款",
          TRD_D_RCG: "订单详情 - 充值",
          TRD_D_RID: "订单详情 - 乘车",
          TRD_D_CON: "订单详情 - 消费",
        },
        tripList: {
          TAB_DONE: "完成",
          TAB_TRIP: "行程中",
          PULL_START: "下拉刷新",
          PULL_DONE: "Pull done",
          DONW_REF_START: "Down",
          DONW_REF_DONE: "f@ck u",
          IN_STA_TIME: "InTime",
          OUT_STA_TIME: "OutTime",
          SCAN_TIME: "Scan time",
          FLG_MTR: "Metro - ",
          FLG_BUS: "Bus - ",
          S_TRIP_SUP: "Supplement",
          S_TRIP_PAY: "Now pay",
          S_TRIPING: "Triping",
          S_TRIP_DONE: "Done",
          S_TRIP_NOIN: "Not in",
          S_TRIP_NOOUT: "Not out",
          S_TIME_OUT: "Time out",
        },
        tripDetail: {
          S_TRIPING: "Triping",
          S_UNPAID: "Unpaid",
          S_PAID: "Trip paid",
          S_SUP_SUBMIT: "Supplement submit",
          S_PAY_SUBMIT: "Submission of pay",
          T_OPS_1: "Select you out station",
          T_OPS_2: "Pay for you trip",
          T_OPS_91: "Pay done",
          T_OPS_92: "Pay done",
          B_RIDE_LINE: "BUS Line",
          B_RIDE_STA: "BUS Station",
          REFUND_LINK: "Trip refunded, learn more>>",
          PAID_FAIL_REA: "Paid fail reason:",
          FEEDBACK_BTN: "Feedback",
          T_SELECT_STA: "Plz select station",
          S_HANDING: "Handing",
          S_SUP_DONE: "Supplement submit",
          S_SUP_ERR: "Supplement fial,",
          S_PAY_DONE: "Pay submit",
          S_PAY_ERR: "Pay fial,",
          S_RFD_LK_FAIL: "Sorry,Query fail",
          TRIP_LOAD_ERR: "Trip load fail",
          BTN_SELECT_STA: "Select",
          BTN_RESELECT_STA: "Reselection",
          BTN_SUP_SUBMIT: "Supplement",
          BTN_PAY_SUBMIT: "Pay",
        },
        tradeList: {
          T_RECG_C: "CountRecharge",
          T_RECG_A: "AmountRecharge",
          T_RECG: "Recharge",
          T_RIDE: "Trip",
          T_COMS: "Consume",
          MENU_RIDE: "Trip",
          MENU_NORMAL: "Consume",
          MENU_RECG: "Recharge",
          TYPE_CLASS: "Classify",
          TRD_SUC: "Trade success",
          TRD_FAIL: "Trade fail",
          TRD_RFD: "Trade Refund",
          TRD_RVK: "Trade revoke",
          TRD_CANCEL: "Trade cancel",
          PAY_FAIL: "Paid fail",
          PAYING: "In payment",
          N_RFD: "Refund",
          MONTH: "Month",
          NOW_MONTH: "Current",
        },
        tradeDetail: {
          STATUS: "Status",
          PAY_TIME: "Paytime",
          TRD_STATUS: "TradeStatus",
          TRD_TIME: "TradeTime",
          PAYMENT: "Payment",
          TRADE_ID: "TradeID",
          TRADE_DTL: "Details",
          RFD_TIME: "RefundTime",
          RFD_MENT: "Refundment",
          RFD_ID: "RefundID",
          ORG_ORDER: "OriginOder",
          ACT_PAY: "ActualPay",
          DISCOUNT: "Discount",
          ASS_RFD_ORD: "Associated refund",
          PKL_PAY: "Parkinglot Pay",
          UN_ASS_TRP: "Unknow trip",
          BTN_VIEW: "View",
          T_R_MTR: "Metro",
          T_R_BUS: "Bus",
          T_R_PKL: "Parkinglot",
          T_R_RCG: "Recharge",
          T_D_RFD: "Refund",
        },
        tradeTextMap: {
          SID_101: "Recharge-amount",
          SID_102: "Recharge-count",
          SID_201: "Pay for trip",
          SID_202: "Pay for trip",
          SID_203: "Pay for trip",
          SID_301: "Refund-trip",
          SID_302: "Refund-trip",
          SID_303: "Refund-amount",
          SID_304: "Refund-count",
          SID_305: "Refund-underAmount",
          SID_306: "Refund-trip",
          SID_307: "Refund-Cashier",
          SID_401: "Cashier",
          SID_04: "Parklot",
        },
        orderStatusMap: {
          RECG_SUC: "Recharge success",
          ORDER_CREATE: "Order create",
          ORDER_HANDING: "Order handing",
          TRADE_SUC: "Trade success",
          TRADE_FAIL: "Trade fail",
          ORDER_CLOSE: "Order close",
          PAY_SUC: "Pay success",
          RFD_SUC: "Refund success",
          S_311: "Trade success",
          S_312: "Trade failed",
          S_313: "In payment",
          S_314: "Trade refunde",
          S_315: "Trade revoke",
          S_316: "Trade revoke",
        },
        orderPayModuleMap: {
          ALI_PAY: "AliPay",
          UNION_PAY: "UnionPay",
          AMOUNT: "Amount",
          WECHAT_PAY: "WechatPay",
          COUNT: "count",
          QRCODE_CUS: "Qrcode",
          UNKNOWN: "Unknown",
        },
        refundDescMap: {
          R_301: "Amount consume Refund",
          R_302: "Couting consume Refund",
          R_303: "Amount recharge Refund",
          R_304: "Counting recharge Refund",
          R_305: "Amount Refund",
          R_306: "Trip paid Refund",
          R_307: "Cashier Refund",
          R_311: "Paid success",
          R_312: "Paid fail",
          R_313: "In payment",
          R_314: "Refund",
          R_315: "Trade revoke",
          R_316: "Trade cancel",
        },
        orderDescMap: {
          D_101: "Amount recharge",
          D_102: "Count recharge",
          D_201: "Amount consume",
          D_202: "Counting card consume",
          D_203: "TideCard consume",
          D_204: "QrCode consume",
          D_301: "Refund for Amount",
          D_302: "Refund for Counting card",
          D_303: "Refund for Amount rechanrge",
          D_304: "Refund for Counting card",
          D_305: "Refund for Amount offline",
          D_306: "Refund for TideCard",
        },
        cityMap: {
          CN_3202: "Wuxi",
          CN_3301: "Hangzhou",
          CN_6401: "Yinchuan",
          CN_12: "Tianjin",
          CN_5101: "Chengdu",
          CN_3502: "Xiamen",
          CN_4113: "Nanyang",
          CN_3404: "Huainan",
          CN_4501: "Nanning",
          CN_4107: "Xinxiang",
          CN_350782: "Wuyishan",
          CN_2102: "Dalian",
          CN_5301: "Kunming",
          CN_3601: "Nanchang",
          CN_3100: "Shanghai",
          CN_3302: "Ningbo",
          CN_3201: "Nanjing",
          CN_NAGOYA: "Nagoya",
          CN_HK: "Hongkong",
          CN_SGA: "Singapore",
        },
        weeks: {
          MON: "Monday",
          TUE: "Tuesday",
          WED: "Wednesday",
          THU: "Thursday",
          FRI: "Friday",
          SAT: "Saturday",
          SUN: "Sunday",
        },
      };
    },
    mzja: function (t, e, n) {
      "use strict";
      var a = n("/kga"),
        i =
          (a.a,
          Boolean,
          String,
          String,
          String,
          Boolean,
          String,
          String,
          Number,
          String,
          {
            name: "alert",
            components: { XDialog: a.a },
            created: function () {
              void 0 !== this.value && (this.showValue = this.value);
            },
            props: {
              value: Boolean,
              title: String,
              content: String,
              buttonText: String,
              hideOnBlur: { type: Boolean, default: !1 },
              maskTransition: { type: String, default: "vux-mask" },
              dialogTransition: { type: String, default: "vux-dialog" },
              maskZIndex: [Number, String],
            },
            data: function () {
              return { showValue: !1 };
            },
            methods: {
              _onHide: function () {
                this.showValue = !1;
              },
            },
            watch: {
              value: function (t) {
                this.showValue = t;
              },
              showValue: function (t) {
                this.$emit("input", t);
              },
            },
          }),
        r = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "div",
              { staticClass: "vux-alert" },
              [
                n(
                  "x-dialog",
                  {
                    attrs: {
                      "mask-transition": t.maskTransition,
                      "dialog-transition": t.dialogTransition,
                      "hide-on-blur": t.hideOnBlur,
                      "mask-z-index": t.maskZIndex,
                    },
                    on: {
                      "on-hide": function (e) {
                        t.$emit("on-hide");
                      },
                      "on-show": function (e) {
                        t.$emit("on-show");
                      },
                    },
                    model: {
                      value: t.showValue,
                      callback: function (e) {
                        t.showValue = e;
                      },
                      expression: "showValue",
                    },
                  },
                  [
                    n("div", { staticClass: "weui-dialog__hd" }, [
                      n("strong", { staticClass: "weui-dialog__title" }, [
                        t._v(t._s(t.title)),
                      ]),
                    ]),
                    t._v(" "),
                    n(
                      "div",
                      { staticClass: "weui-dialog__bd" },
                      [
                        t._t("default", [
                          n("div", {
                            domProps: { innerHTML: t._s(t.content) },
                          }),
                        ]),
                      ],
                      2
                    ),
                    t._v(" "),
                    n("div", { staticClass: "weui-dialog__ft" }, [
                      n(
                        "a",
                        {
                          staticClass:
                            "weui-dialog__btn weui-dialog__btn_primary",
                          attrs: { href: "javascript:;" },
                          on: { click: t._onHide },
                        },
                        [t._v(t._s(t.buttonText || "确定"))]
                      ),
                    ]),
                  ]
                ),
              ],
              1
            );
          },
          staticRenderFns: [],
        };
      var o = n("VU/8")(
        i,
        r,
        !1,
        function (t) {
          n("kp3f");
        },
        null,
        null
      );
      e.a = o.exports;
    },
    qKOS: function (t, e) {},
    rHil: function (t, e, n) {
      "use strict";
      var a = n("wmxo"),
        i =
          (a.a,
          String,
          String,
          String,
          String,
          String,
          String,
          Number,
          String,
          String,
          {
            name: "group",
            methods: { cleanStyle: a.a },
            props: {
              title: String,
              titleColor: String,
              labelWidth: String,
              labelAlign: String,
              labelMarginRight: String,
              gutter: [String, Number],
              footerTitle: String,
              footerTitleColor: String,
            },
          }),
        r = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "div",
              [
                t.title
                  ? n("div", {
                      staticClass: "weui-cells__title",
                      style: t.cleanStyle({ color: t.titleColor }),
                      domProps: { innerHTML: t._s(t.title) },
                    })
                  : t._e(),
                t._v(" "),
                t._t("title"),
                t._v(" "),
                n(
                  "div",
                  {
                    staticClass: "weui-cells",
                    class: { "vux-no-group-title": !t.title },
                    style: t.cleanStyle({
                      marginTop:
                        "number" == typeof t.gutter
                          ? t.gutter + "px"
                          : t.gutter,
                    }),
                  },
                  [t._t("after-title"), t._v(" "), t._t("default")],
                  2
                ),
                t._v(" "),
                t.footerTitle
                  ? n("div", {
                      staticClass: "weui-cells__title vux-group-footer-title",
                      style: t.cleanStyle({ color: t.footerTitleColor }),
                      domProps: { innerHTML: t._s(t.footerTitle) },
                    })
                  : t._e(),
              ],
              2
            );
          },
          staticRenderFns: [],
        };
      var o = n("VU/8")(
        i,
        r,
        !1,
        function (t) {
          n("wsKR");
        },
        null,
        null
      );
      e.a = o.exports;
    },
    rLAy: function (t, e, n) {
      "use strict";
      var a = n("xNvf"),
        i =
          (a.a,
          Boolean,
          Number,
          String,
          String,
          String,
          Boolean,
          String,
          String,
          {
            name: "toast",
            mixins: [a.a],
            props: {
              value: Boolean,
              time: { type: Number, default: 2e3 },
              type: { type: String, default: "success" },
              transition: String,
              width: { type: String, default: "7.6em" },
              isShowMask: { type: Boolean, default: !1 },
              text: String,
              position: String,
            },
            data: function () {
              return { show: !1 };
            },
            created: function () {
              this.value && (this.show = !0);
            },
            computed: {
              currentTransition: function () {
                return this.transition
                  ? this.transition
                  : "top" === this.position
                  ? "vux-slide-from-top"
                  : "bottom" === this.position
                  ? "vux-slide-from-bottom"
                  : "vux-fade";
              },
              toastClass: function () {
                return {
                  "weui-toast_forbidden": "warn" === this.type,
                  "weui-toast_cancel": "cancel" === this.type,
                  "weui-toast_success": "success" === this.type,
                  "weui-toast_text": "text" === this.type,
                  "vux-toast-top": "top" === this.position,
                  "vux-toast-bottom": "bottom" === this.position,
                  "vux-toast-middle": "middle" === this.position,
                };
              },
              style: function () {
                if ("text" === this.type && "auto" === this.width)
                  return { padding: "10px" };
              },
            },
            watch: {
              show: function (t) {
                var e = this;
                t &&
                  (this.$emit("input", !0),
                  this.$emit("on-show"),
                  this.fixSafariOverflowScrolling("auto"),
                  clearTimeout(this.timeout),
                  (this.timeout = setTimeout(function () {
                    (e.show = !1),
                      e.$emit("input", !1),
                      e.$emit("on-hide"),
                      e.fixSafariOverflowScrolling("touch");
                  }, this.time)));
              },
              value: function (t) {
                this.show = t;
              },
            },
          }),
        r = {
          render: function () {
            var t = this,
              e = t.$createElement,
              n = t._self._c || e;
            return n(
              "div",
              { staticClass: "vux-toast" },
              [
                n("div", {
                  directives: [
                    {
                      name: "show",
                      rawName: "v-show",
                      value: t.isShowMask && t.show,
                      expression: "isShowMask && show",
                    },
                  ],
                  staticClass: "weui-mask_transparent",
                }),
                t._v(" "),
                n("transition", { attrs: { name: t.currentTransition } }, [
                  n(
                    "div",
                    {
                      directives: [
                        {
                          name: "show",
                          rawName: "v-show",
                          value: t.show,
                          expression: "show",
                        },
                      ],
                      staticClass: "weui-toast",
                      class: t.toastClass,
                      style: { width: t.width },
                    },
                    [
                      n("i", {
                        directives: [
                          {
                            name: "show",
                            rawName: "v-show",
                            value: "text" !== t.type,
                            expression: "type !== 'text'",
                          },
                        ],
                        staticClass:
                          "weui-icon-success-no-circle weui-icon_toast",
                      }),
                      t._v(" "),
                      t.text
                        ? n("p", {
                            staticClass: "weui-toast__content",
                            style: t.style,
                            domProps: { innerHTML: t._s(t.text) },
                          })
                        : n(
                            "p",
                            {
                              staticClass: "weui-toast__content",
                              style: t.style,
                            },
                            [t._t("default")],
                            2
                          ),
                    ]
                  ),
                ]),
              ],
              1
            );
          },
          staticRenderFns: [],
        };
      var o = n("VU/8")(
        i,
        r,
        !1,
        function (t) {
          n("0nrA");
        },
        null,
        null
      );
      e.a = o.exports;
    },
    wsKR: function (t, e) {},
    z3SG: function (t, e) {},
  },
  ["NHnr"]
);
//# sourceMappingURL=app.ed57ec4f925421679b80.js.map
