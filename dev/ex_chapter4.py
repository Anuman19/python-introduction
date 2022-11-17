a = ('Peter','Hans', 'Fred', 'Hans', 'Ursula', 'Robert', 'Ursula', 'Hans')
d = {}

for i in a:
    if i not in d.keys():
        d[i] = a.count(i)
        
for k, v in d.items():
    print(k, v)
        