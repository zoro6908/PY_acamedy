from flask import Flask as fk
from flask import render_template as rt

app = fk(__name__)

@app.route("/")
def temp_test():
    return rt("ExPy70802.html", my_string="템플릿 테스트", my_list=['바나나','오렌지','고구마'])

if __name__ == '__main__':
    app.run()

