from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/ex/env", methods=["GET", "POST"])
def ex():
    return("path : %s<br/>"
           "url : %s<br/>"
           "baseurl : %s<br/>"
           "url_root : %s<br/>"
           ) % (request.path, request.url, request.base_url, request.url_root)

if __name__ == '__main__':
    app.run()
