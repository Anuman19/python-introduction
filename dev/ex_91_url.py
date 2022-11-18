import urllib.request as req

url = req.urlopen("http://www.cssgmbh.ch/cssgmbh/Beispiele/url_lesen.htm")

list = url.readlines()

url.close()

for line in list:
    if "Python" in str(line):
        print(line)
    else:
        print("no")

u = req.urlopen("http://www.cssgmbh.ch/cssgmbh/Beispiele/senden_get.php?nn=Muster&vn=Max")

ulist = u.readlines()
u.close()

for line in ulist:
    print(str(line))
    
import webbrowser

print(webbrowser.open("http://www.digicomp.ch"))
print()

wiki = req.urlopen("https://de.wikipedia.org/wiki/Schweiz")
wikiList =   wiki.readlines()
wiki.close()

cities = {"Bern", "Zürich", "Basel", "Genf", "Luzern", "Uri"}
s = []
for line in wikiList:
    for word in str(line).split():
        if str(word) in cities:
            #s.append(str(word))
            s.append(str(word))
        
for city in cities:
    print(city, s.count(city))
