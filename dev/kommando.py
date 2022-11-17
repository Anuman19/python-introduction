import sys
print("Parameter:", sys.argv)
print("Anzahl:", len(sys.argv))

sum = 0

for i in sys.argv[1:]:
    try:
        sum += float(i)
    except:
        print("Error bei:", i)

print("sum:", sum)