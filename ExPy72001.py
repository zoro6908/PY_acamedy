from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def test_app():
    return render_template("ExPy72001.html", title="Main", my_body="메인 페이지")

if __name__ == '__main__':
    app.run()