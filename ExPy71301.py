from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def html_render():
    return render_template("ExPy71301c.html", my_string="안녕하세요", my_list=[111,222,333,444,555])

if __name__ == '__main__':
    app.run(debug=True)
