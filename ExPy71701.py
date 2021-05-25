from jinja2 import FileSystemLoader
from jinja2 import Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

temp1 = env.get_template("ExPy71701.html")
# temp1 = env.get_template("ExPy71601c.html")
print(temp1.render())