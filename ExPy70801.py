# [ 8 차시 ] Jinja2 템플릿 엔진 표현식

from jinja2 import Template

temp = Template("Hello {{name}}~~~")
print(temp.render(name="kim"))

temp = Template("number : {% for n in range(1, 10) %} {{n}} {% endfor %}")
print(temp.render())
