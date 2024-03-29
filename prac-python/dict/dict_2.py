from typing import Dict

def add_to_dict(dict: Dict, input: str):
    dict[input] = input

dict_0 = {}

add_to_dict(dict_0, "1")
add_to_dict(dict_0, "2")
add_to_dict(dict_0, "3")


for element in dict_0:
    print(element)


dict_1 = {}

dict_1["a"] = 0
dict_1["b"] = {"bb": "bbb"}
# does not work, KeyError
# dict_1["c"]["d"] = [2]
dict_1["c"] = {"d": [2]}
dict_1["c"]["d"].append(3)

e_exists = dict_1.get("e")
print(e_exists)

if e_exists:
    print("can use e")
else:
    print("can not use e")

if not dict_1.get("not_exists"):
    print("not exists")
else:
    print("does exists")

if True and dict_1.get("f"):
    print("can use f")
else:
    print("can not use f")

if "g" not in dict_1:
    dict_1["g"] = {"h": ["i", "g"]}

if "b" in dict_1 and dict_1["b"].get("bbbb") is None:
    dict_1["b"]["bbbb"] = ["bbbbb"]

if "t" not in dict_1:
    dict_1["t"] = {"n": ["g"]}

if "t" in dict_1 and dict_1["t"].get("c") is None:
    dict_1["t"]["c"] = ["v"]

dict_1["t"]["c"].append("d")

print("elements of dict_1")
for element in dict_1:
    print("{} - {}".format(element, dict_1[element]))

print("len of dict_1: {}".format(len(dict_1)))

print(dict_1)