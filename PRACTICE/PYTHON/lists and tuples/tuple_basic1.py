num = (1,4,2,7)

print(num[-1])

print(num)
print(num[4:1])

#convert tuple to list and then tuple

num1 = [7,5,2,9,0]

tuple1  = tuple(num1)
print(num1)
print(tuple1)

#Unpacking
a,*b,c,d = num1  
print(a, b,c,d)
num2 = [1,2]

a,b = num2
print(a,b)