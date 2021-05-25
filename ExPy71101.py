from jinja2 import FileSystemLoader
from jinja2 import Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

temp1 = env.get_template("ExPy71101a.txt")
print(temp1.render())

temp2 = env.get_template("ExPy71101b.txt")
print(temp2.render())

print(temp2.render(name="김사장", animal="고양이"))

temp3 = env.get_template("ExPy71101c.txt")

# person = {"김사장":"500만원", "이사장":"300만원"}
person = {}
person['name'] = "김사장"
person['salary'] = 2000

print(temp3.render(data=person))