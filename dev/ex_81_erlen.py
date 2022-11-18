import re

d = open("Erlkoenig.txt")

lines = d.readlines()
d.close()

new = open("Erlkoenig2.txt", "w")


for line in lines:
    print(line.rstrip())
    new.write(re.sub('^er', 'Er', line, 1))

new.close()

new = open("Erlkoenig2.txt")

newLines = new.readlines()

new.close()

print()
for line in newLines:
    print(line.rstrip())
    
