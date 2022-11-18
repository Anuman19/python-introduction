print("{0:<4}{1:>9}{2:>4}{3:>4}{4:>8}".format("dez", "dual", "okt", "hex", "float"))
fm="{0:<4d}{1:>9b}{2:>4o}{3:>4x}{4:>8.2f}"
for z in range(62,66):
    print(fm.format(z,z,z,z,z))
    
print()
    
print("{0:<8}{1:<8}{2:>8}".format("Von", "Nach", "Distanz"))
fz = "{0:<8}{1:<8}{2:>8.2f}"
dist = [125, 51.4, 85.2]
city = ["Zürich", "Bern", "Luzern", "Basel"]
for i in range(len(dist)):
    print(fz.format(city[0],city[i+1], dist[i]) + " km")
