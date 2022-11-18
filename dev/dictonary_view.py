age = {"Peter": 31, "Julia":28, "Werner": 35}
print(age)
print()

val = age.values()
key = age.keys()
item = age.items()

print(type(val), type(key), type(item))
print(val)
print(key)
print(item)

print("age")

for i in age:
    print(i)

print("val")

for i in val:
    print(i)

print("key")

for i in key:
    print(i)
    
print("item")

for i in item:
    print(i)
    