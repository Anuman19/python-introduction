import re

x = "dies ist mein Haus und dies ist dein Haus"

print(x)
print(re.sub('dies', "Dies", x, 1))
print(re.sub("Haus$",  "Stall", x))
x = re.sub('dies', "Dies", x, 1)
x= re.sub("Haus$",  "Stall", x)

print(x + ".")

