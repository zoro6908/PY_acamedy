from jinja2 import FileSystemLoader
from jinja2 import Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

temp1 = env.get_template("ExPy71901.html")

userData = [{"user_name":"hong", "name":"홍길동", "job":"회사원"},
            {"user_name":"jung", "name":"정수근", "job":"야구선수"},
            {"user_name":"son", "name":"손홍민", "job":"축구선수"}]

print(temp1.render(user_list=userData))
