from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/abab", methods=["GET", "POST"])
def abab():
    # return request.values.get("name") //오류 발생
    # 브라우저에서 변수 값이 넘어오지 않았을 경우 기본값을 정의할 수 있다.
    return request.values.get("name", "전달된 데이터가 없습니다.~~~~")

if __name__ == '__main__':
    app.run()
