z = [3000, "Bern", 1200, "Lausanne"]
for x in z:
    print(x)
z.append(8000)
print(z)
print(z[0])
print(z[3])

print()

x = [[3000, "Bern"], [1200, "Genf"]]
print(x)
print(x[0])
print(x[1][1])
x.append([1,2])
print(x)

print()

v = [30, 5, 10, "Tag"]
v.append(8)

print(v[-2])