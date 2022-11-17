import random

# Standard Lambda-Funktion
kreisfläche = lambda r: r**2*3.14
print(kreisfläche(3))
# Lambda mit map-Funktion
f = list(map(lambda r: (r**2), [3,5,12]))
print(f)
# Lambda mit filter-Funktion
ungrad = list(filter(lambda x: x % 2,
[random.randint(1,1000) for i in range(10)]))
print(ungrad)