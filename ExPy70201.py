from flask import Flask, __main__

app = Flask(__name__)

@app.route("/user/<userName>")
def get_user(userName):
    return ("User Name :" +userName)

if __name__ == "__main__":
    app.run()