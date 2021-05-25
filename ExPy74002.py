from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def res():
    res = Response("응답 테스크")
    res.set_data("플라스크 학습하기")
    return res

if __name__ == '__main__':
    app.run()
