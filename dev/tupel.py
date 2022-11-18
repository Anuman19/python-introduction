import sys

z = (3, 6, -8, 5.5)
print(z)

print(sys.getsizeof(z))

x = (("Paris", "Fr", 350, ["Rom", "It", 420]))
print(x)
print(sys.getsizeof(x))


print()



v = (20, "Haus", 1, "Baum")
print(v[1])
test, test1 = v[:2]
#print(test, test1)
try:
    print(v[len(v) -1])
    t = []
    t[len(t) -1] = "Test"
    print(t)
    v[len(v) -1] = "Test"
    
except Exception as e:
    print(e)