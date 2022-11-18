dic = {1234-1:"Zopf", 2345-1:"Gipfeli", 3456-1:"Tessiner", 4567-1: "Weggli"}

print("Art.Nr", "Artikel")
for k, v in dic.items():
    
    print(k, v)
    

pos={}
pos['Käfigturm']=(200,280,120,150)
pos['Zytglogge']=(410,490,140,160)

print(pos)

print(list(pos.values())[1][0])