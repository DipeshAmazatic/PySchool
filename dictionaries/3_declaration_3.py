# Dictionary consists of key-value data pair. Python provides a few ways to add/update key-value pair.
# Suppose "d" is an empty dictionary, which statement does not assign "d" with {"Name":"Tom"}?

d={}
d = {"Name": "Tom" }
d["Name"] = "Tom"
d.update({"Name": "Tom" })
d.setdefault("Name", "Tom")
## all are valid