from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_world():
    return "<h1>Hellow Wrold</h1>"

# String타입의 userName 파라미터
# String 타입은 기본값이다.
@app.route("/user/<userName>")
def show_user(userName):
    return "User {}".format(userName)
    # return "User %s" %userName

# int type의 post_id 파라미터
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id

# float타입의 pi파타미터
@app.route("/circle/<float:pi>")
def show_pi(pi):
    return "pi %f" % pi

if __name__ == "__main__":
    app.run()