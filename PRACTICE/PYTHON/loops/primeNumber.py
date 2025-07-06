number = int(input("Enter number to check the number is prime or not !"))
isprime = False
for i in range(2,number):
    if(number%i==0):
        isprime = True
        exit
        
if(isprime):
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")
    
