# 1)creating a dictionary
my_dict={"name":"ardra","age":21,"place":"pandikkad"}
print(my_dict)

another_dict=dict(name="ardra",age=21,place="pandikkad")
print(another_dict)

#empty dictionary
empty_dict={}
print(empty_dict)

# 2)accessing dictionary items
#accessing with brackets
my_dict={"name":"john","age":30}
print(my_dict["name"])
#using get
my_dict={"name":"john","age":30}
print(my_dict.get("age"))

# 3)changing dictionary items
my_dict={"name":"john","age":30}
my_dict["age"]=31
print(my_dict)

# 4)adding items to a dictionary
my_dict={"name":"john","age":30}
my_dict["city"]="new york"
print(my_dict)

# 5)removing items from a dictionary
#pop(key)
my_dict={"name":"john","age":30,"city":"new york"}
age=my_dict.pop("age")
print(age)

#popitem()
my_dict={"name":"john","age":30}
last_item=my_dict.popitem()
print(last_item)

#del statement
my_dict={"name":"john","age":30}
del my_dict["age"]
print(my_dict)

#clear()
my_dict={"name":"john","age":30}
my_dict.clear()
print(my_dict)

# 6)copying a dictionary
#using copy()
original={"name":"john","age":30}
copy_dict=original.copy()
print(copy_dict)

#using dict() constructor
original={"name":"john","age":30}
copy_dict=dict(original)
print(copy_dict)

# 7)nested dictionaries
my_dict={
    "a":{"name":"john","age":30},
    "b":{"name":"ardra","age":21}
}
print(my_dict["b"]["name"])

# 8)dictionary methods
#keys()
my_dict={"name":"john","age":30}
print(my_dict.keys())

#values()
my_dict={"name":"john","age":30}
print(my_dict.values())

#items()
my_dict={"name":"john","age":30}
print(my_dict.items())

#update()
my_dict={"name":"john","age":30}
my_dict.update({"city":"new york","age":21})
print(my_dict)

#fromkeys()
keys=["name","age","city"]
new_dict=dict.fromkeys(keys,"ardra")
print(new_dict)

#setdefault(key,value)
my_dict={"name":"john","age":30}
city=my_dict.setdefault("city","new york")
print(city)
print(my_dict)