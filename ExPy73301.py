from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/aaa/")
def aaa():
    return "request객체를 이용하여 가져온 name의 변수 값은 {}입니다.".format(request.args.get("name"))

if __name__ == '__main__':
    app.run()
