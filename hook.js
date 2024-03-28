_Function = Function.prototype.constructor;
Function.prototype.constructor = function (val) {
  if(val === "debugger"){
    return ""
  }
  return _Function(this, val)
}



_cookie = document.cookie
Object.defineProperty(document, "cookie", {
  get() {
    return _cookie
  },
  set(v) {
    debugger;
    _cookie = v
    return _cookie;
  }
})
