from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

class userDateType:
    def __init__(self, format):
        self.format = format
    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)

@app.route("/eee", methods=["GET", "POST"])
def eee():
    print(request.values.getlist("dates", type=userDateType("%Y-%m-%d")))
    return "콘솔을 통해 확인해 주세셩~~~~~"

if __name__ == '__main__':
    app.run()




