from jinja2 import FileSystemLoader
from jinja2 import Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

# temp1 = env.get_template("ExPy71201a.txt")
# print(temp1.render(truth=True))
# print(temp1.render(truth=False))

temp2 = env.get_template("ExPy71201b.txt")
cls = ["발강", "노랑", "파랑"]
print(temp2.render(colors=cls))


