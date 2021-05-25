from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/bbb/")
def bbb():
    params = request.args.to_dict()
    param = ""

    for key in params.keys():
        param += "key : {}, value : {}\n".format(key, request.args[key])
    return param

if __name__ == '__main__':
    app.run()