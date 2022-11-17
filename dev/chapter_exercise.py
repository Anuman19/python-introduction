import random



def payment():
    bill = random.randint(10,100)
    print("The bill is", bill)

    pay = int(input("Insert your payment:\n"))
    
    result = bill - pay
        
    if result > 0:
        print("Rest is", result)
    elif result < 0:
        print("Balance", abs(result))
    else:
        print("Nicely done")
            

while True:
    try:
        payment()
    except Exception as e:
        print(e)
        continue
    run = input("Press 0 to end\n")
    if run == "0":
        break

    
        