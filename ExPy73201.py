from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/aaa/", redirect_to="/new_aaa/")
def aaa():
    return "/aaa/로 호출한 페이지입니다."

@app.route("/new_aaa/")
def new_aaa():
    return "/new_aaa/로 호출한 페이지입니다."

if __name__ == '__main__':
    app.run()

