from werkzeug.datastructures import MultiDict

md = MultiDict()

md.add("ani", "dog")

print(md)
print(md.get("ani"))
print(md)
print(md.pop("ani"))
print(md)

md1 = MultiDict()

md1.setlist("ani", ["dog", "cat"])

print(md1)
print(md1.getlist("ani"))
print(md1.poplist("ani"))
print(md1)

md.add("ani", "dog")
md1.add("name", "hong")
md.update(md1)
print(md)

