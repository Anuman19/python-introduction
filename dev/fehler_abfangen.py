z = input("Enter a number ")

try:
    z = int(z)
    print("Nice")
    print(z+5)
except Exception as e:
    print("No")
    print(e)