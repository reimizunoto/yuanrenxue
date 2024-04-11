(function () {
  var g = function () {
    var p = !![];
    return function (q, r) {
      var s = p ? function () {
        if (r) {
          var t = r["apply"](q, arguments);
          r = null;
          return t;
        }
      } : function () {};
      p = ![];
      return s;
    };
  }();
  var h = g(this, function () {
    var n = function () {
      var o = n["constructor"]("return /\" + this + \"/")()["compile"]("^([^ ]+( +[^ ]+)+)+[^ ]}");
      return !o["test"](h);
    };
    return n();
  });
  h();
  var j = function () {
    var p = !![];
    return function (q, r) {
      var s = p ? function () {
        if (r) {
          var t = r["apply"](q, arguments);
          r = null;
          return t;
        }
      } : function () {};
      p = ![];
      return s;
    };
  }();
  (function () {
    j(this, function () {
      var q = new RegExp("function *\\( *\\)");
      var r = new RegExp("\\+\\+ *(?:[a-zA-Z_$][0-9a-zA-Z_$]*)", "i");
      var s = $c("init");
      if (!q["test"](s + "chain") || !r["test"](s + "input")) {
        s("0");
      } else {
        $c();
      }
    })();
  })();
  var k = function () {
    var p = !![];
    return function (q, r) {
      var s = p ? function () {
        if (r) {
          var v = r["apply"](q, arguments);
          r = null;
          return v;
        }
      } : function () {};
      p = ![];
      return s;
    };
  }();
  var l = k(this, function () {
    var n = function () {};
    var o;
    try {
      var p = Function("return (function() " + "{}.constructor(\"return this\")( )" + ");");
      o = p();
    } catch (u) {
      o = window;
    }
    if (!o["console"]) {
      o["console"] = function (w) {
        var B = {};
        B["log"] = w;
        B["warn"] = w;
        B["debug"] = w;
        B["info"] = w;
        B["error"] = w;
        B["exception"] = w;
        B["table"] = w;
        B["trace"] = w;
        return B;
      }(n);
    } else {
      o["console"]["log"] = n;
      o["console"]["warn"] = n;
      o["console"]["debug"] = n;
      o["console"]["info"] = n;
      o["console"]["error"] = n;
      o["console"]["exception"] = n;
      o["console"]["table"] = n;
      o["console"]["trace"] = n;
    }
  });
  l();
  try {
    if (global) {
      if (true) {
        decrypt("1712743002");
      } else {
        decrypt("1712743002");
      }
    }
  } catch (o) {
    global = new Array();
  }
  window = new Array();
  for (var m = 0x1; m <= 3; m++) {
    res = decrypt("1712743002") + "r";
  }
  document["cookie"] = "m=" + (m - 0x1)["toString"]() + res + "; path=/";
})();
setInterval(function () {
  $c();
}, 0xfa0);
function $c(b) {
  function e(f) {
    if (typeof f === "string") {
      return function (i) {}["constructor"]("while (true) {}")["apply"]("counter");
    } else {
      if (("" + f / f)["length"] !== 0x1 || f % 0x14 === 0x0) {
        (function () {
          return !![];
        })["constructor"]("debu" + "gger")["call"]("action");
      } else {
        (function () {
          return ![];
        })["constructor"]("debu" + "gger")["apply"]("stateObject");
      }
    }
    e(++f);
  }
  try {
    if (b) {
      return e;
    } else {
      e(0x0);
    }
  } catch (i) {}
}