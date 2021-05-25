from flask import Flask
from flask import request
from datetime import datetime

# 사용자 정의 함수 : 특정 날짜 형식을 지정
def userDateType(date_format):
    def changeFormat(date_string):
        # strptime(date_string, fortmat) : format에 맞게 date_string을 datetime객체로 리턴
        return datetime.strptime(date_string, date_format)
    return changeFormat

app = Flask(__name__)
@app.route("/ccc", methods=["GET", "POST"])
def ccc():
    print(request.values.get("date", default="2021/05/18", type=userDateType("%Y-%m-%d")))
    return "콘솔을 통해 확인해 보세요~~~"

if __name__ == '__main__':
    app.run()

