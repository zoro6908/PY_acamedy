from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def bs_test():
    return render_template("ExPy71002.html")

if __name__ == '__main__':
    app.run(debug=True)
