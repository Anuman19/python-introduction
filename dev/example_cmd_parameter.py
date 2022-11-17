import sys

argc=len(sys.argv)
if argc==1:
    print("Keine Sprache ausgewählt")
else:
    for w in range(1, argc):
        if "f" in sys.argv[w]:
            print("Bonjour")
        elif "e" in sys.argv[w]:
            print("G'day")
        else:
            print("Gute Tag")
            
