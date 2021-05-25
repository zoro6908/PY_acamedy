from jinja2 import FileSystemLoader
from jinja2 import Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

# temp1 = env.get_template("ExPy71202a.html")
# print(temp1.render(title="반갑습니다. 파이선"))
temp1 = env.get_template("ExPy71202c.html")
print(temp1.render(title="반갑습니다. 파이선", body="상속연습"))