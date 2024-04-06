_Function = Function.prototype.constructor;
Function.prototype.constructor = function (val) {
  if(val === "debugger"){
    return ""
  }
  return _Function(this, val)
}



let _cookie = document.cookie
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


Object.defineProperty(document, "cookie", {
  get(val) {
    let get_func = Object.getOwnPropertyDescriptor(Document.prototype,'cookie')['get'];
    return get_func().call(this, val)
  },
  set(val) {
    debugger;
    let set_func = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie')['set']
    return set_func.call(this, val)
  }
})

let _ss = window['_$ss'];
Object.defineProperty(window, "_$ss", {
  get() {
    debugger;
    return _ss;
  },
  set(v) {
    debugger;
    _ss = v;
    return _ss;
  }
});
