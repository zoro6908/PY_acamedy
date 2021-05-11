from flask import Flask as fk
from flask import url_for as uf

app = fk(__name__)

@app.route("/hello/")
def hello():
    return "<h1>Hellow World</h1>"

@app.route("/user/<username>")
def get_user(username):
    return "User : "+username

if __name__ == '__main__':
    with app.test_request_context():
        print (uf("hello"))
        print (uf("get_user", username = "kimkim"))