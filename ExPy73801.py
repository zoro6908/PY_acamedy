from flask import Flask
from flask import request

app =Flask(__name__)

@app.route("/test/env", methods=["GET", "POST"])
def test():
    strVal = ("REQUEST_METHOD : %(REQUEST_METHOD)s<br/>"
              "PATH_INFO : %(PATH_INFO)s<br/>"
              "QUERY_STRING : %(QUERY_STRING)s<br/>"
              "SERVER_NAME : %(SERVER_NAME)s<br/>"
              "SERVER_PORT : %(SERVER_PORT)s<br/>"
              "SERVER_PROTOCOL : %(SERVER_PROTOCOL)s<br/>"
              "wsgi.version : %(wsgi.version)s<br/>"
              "wsgi.url_scheme : %(wsgi.url_scheme)s<br/>"
              ) % request.environ
    return strVal

if __name__ == '__main__':
    app.run()



