var1 = 100
var2 = 0

if var1:
    print("1 - Got a true expression value")
    print(var1)
elif var2:
    print("2 - Got a true expression value")
    print(var2)
else:
    print("1 - Got a false expression value")
    print(var1)

if var2:
    print("2 - Got a true expression value")
    print(var2)
elif var1 * 0:
    print("1 - Got a true expression value")
    print(var1)
else:
    print("2 - Got a false expression value")
    print(var2)

print("Good bye!")
