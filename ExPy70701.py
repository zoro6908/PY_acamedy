from flask import Flask as fk
from flask import render_template as rt

app = fk(__name__)

@app.route("/")
def hello():
    return  "<h1>Hello World</h1>"

@app.route("/user/<username>/")
def user(username):
    return rt('ExPy70701.html', name=username)

if __name__ == '__main__':
    app.run()
