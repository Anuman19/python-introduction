#!/usr/bin/python3

li = [3] # List
di = {"x":3} # Dictionary
se = {3} # Set

def func1():
    li=[8]; di={"x":5}; se={8}
    print("Func 1:", li, di, se)
    
def func2():
    li[0]=8; di["x"]=5; se.add(8)
    print("Func 2:", li, di, se)

func1()
print("Main 1:", li, di, se)
func2()
print("Main 2:", li, di, se)
print()

zahl = 3 # Integer
text = "Hallo" # String
def func1():
    zahl=5
    text="Ade"
    print("Func 1:", zahl, text)
    
def func2():
    global zahl, text
    zahl=5
    text="Ade"
    print("Func 2:", zahl, text)

func1()
print("Main 1:", zahl, text)
func2()
print("Main 2:", zahl, text)