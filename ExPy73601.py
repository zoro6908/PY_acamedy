from werkzeug.datastructures import MultiDict

md = MultiDict()

# 객체에 키와 값을 추가
md.add("name", "hong")
md.add("date", 2000)

# 객체에 똑같은 키를 갖는 여러개의 값을 추가
md.setlist("dates", [2001, 2002])

# 기존의 키가 있으면 값이 추가 되지 않고 없으면 추가
md.setdefault("name", "kim")
md.setdefault("ani", "dog")
md.setdefault("ani", "cat")
md.setlistdefault("ani", ["dog", "cat", "mouse"])

# 객체에 데이터를 지우고자 할 때
md.clear()



print(md)