s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1)

s2 = s1.copy()
s2.add("tes2")
print(s2)
s1.add("asdf")
print(s1)
s1.discard(1)
print(s1)
s2.clear()
print(s2)
