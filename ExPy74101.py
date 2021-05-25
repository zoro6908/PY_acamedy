from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)
@app.route("/cookie_set")
def cookieSet():
    res = Response("쿠키 생성~~~")
    res.set_cookie("cname", "Flask-Study")
    return res

@app.route("/cookie_del")
def cookieDel():
    res = Response("쿠키 삭제~~~")
    res.set_cookie("cname", expires=0)
    return res

@app.route("/cookie_rev")
def cookieRev():
    res = request.c
    return "cname 쿠키은 %s 값을 가지고 있습니다." % (request.cookies.get("cname", ""))

if __name__ == '__main__':
    app.run()

