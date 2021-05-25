from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

class userDateType():
    def __init__(self, format):
        self.format = format
    def __call__(self, *args, **kw):
        return datetime.strptime(args[0], self.format)

@app.route("/ddd", methods=["GET", "POST"])
def ddd():
    print(request.values.get("date", "2021-05-18", type=userDateType("%Y-%m-%d")))
    return "콘솔에서 확인 바랍니다."

if __name__ == '__main__':
    app.run()


