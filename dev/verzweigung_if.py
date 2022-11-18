running = True

while(True):

    print("Please enter a nunmber")
    x = input("= ")
    x = int(x)

    if x == 50:
        print(x, "your number is 50")
    elif x > 50:
        print(x, "your number is greater than 50")
    else:
        print(x, "your number is smaller than 50")
    print("Go again y/n?")
    running = str(input())
    if running == "y":
        continue
    elif running == "n":
        break
    else:
        print("No")
        break