x = 10

def printNumber():
    global x
    x = 7
    print(f"local x {x}")

print("global x " , x)
printNumber()
print("global x " , x)