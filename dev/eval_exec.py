#e = eval(input("Enter a calculation "))
#print(e)
#print()
t = 'a=[3,6,9]\nfor i in a: print(i)'
exec(t)

print()

print(eval(compile(t, '<string>', 'exec')))