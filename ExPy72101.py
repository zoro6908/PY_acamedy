from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def test_app():
    return render_template("ExPy72101a.html", title="Main", my_body="메인 페이지")

@app.route("/home")
def home():
    return render_template("ExPy72101a.html", title="Home", my_body="홈 페이지")

@app.route("/about")
def about():
    return render_template("ExPy72101a.html", title="About", my_body="소개 페이지")

@app.route("/contact")
def contact():
    return render_template("ExPy72101a.html", title="Contact Us", my_body="문의 페이지")

if __name__ == '__main__':
    app.run()