num = int(input("Enter the number between 1 to 9"))

if(num > 9 or num < 0):
    raise Exception("Number should be between 1 to 9")
else:
    print(num)