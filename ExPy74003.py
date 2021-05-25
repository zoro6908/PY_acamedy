from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def res():
    res = Response("플라스크 쿠키 학습하기")
    res.set_cookie("ID", "Flask-Study")
    return res

if __name__ == '__main__':
    app.run()
