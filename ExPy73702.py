from werkzeug.datastructures import MultiDict

md = MultiDict()

md.add("ani", "dog")
print(md)
md.setlist("ani", ["dig2", "cat"])
print(md)

md1 = MultiDict()

md1.add("ani", ["dig2", "cat"])

md1_copy = md1.copy()
md1_deepcopy = md1.deepcopy()
print(md1_copy)
print(md1_deepcopy)

md1_copy["ani"].append("cat2")
md1_copy["ani"].extend("cat2")
print(md1_copy)

md1_deepcopy["ani"].append("cat3")
md1_deepcopy["ani"].extend("cat3")
print(md1_deepcopy)
print(md1)