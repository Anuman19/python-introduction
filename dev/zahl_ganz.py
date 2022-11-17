a = 12
e = 5.97E+24

print(type(a))
print("dez:", a)
print("hex:", hex(a))
print("oct:", oct(a))
print("bin:", bin(a))
print("float:", float(a))
print(f"Mass: {e} -> {int(e)} kg")

c = 2.5

print(type(c))
print(a - c)
print(a * c)
print(a / c)
print(round(a ** c, 5))
print(0xC + a + 0b1100 + 0o14)

print()

print(float(0x8a + 0b11101))
print(int(1.2))