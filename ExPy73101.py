from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/aaa/<bbs_id>")
@app.route("/aaa/", defaults={"bbs_id":100})
def aaa(bbs_id):
    return "aaa의 {}번째 글입니다.".format(bbs_id)

if __name__ == '__main__':
    app.run()