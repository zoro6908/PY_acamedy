from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def res():
    res = Response("응답 테스크 하기")
    res.headers.add("webApp-Name", "Fask-Test")
    return res

if __name__ == '__main__':
    app.run()
