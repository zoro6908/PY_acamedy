from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def tmeplate_test():
    return render_template("ExPy70901.html", my_string="펨플릿 테스트", my_list=[11,22,33,44,55,66])

if __name__ == '__main__':
    app.run(debug=True)

