age = "19"
print(int(age) )
str1 = 13
print(str(str1))

int(5.99)         # 5
int("10")         # 10
try:
    int("10.5")       # ValueError
    int("abc")        #  ValueError
except:
    print("error")
print("list ans : " , list("hello")) 
print(tuple([1,2,4]))
print(set("hello"))  #only unique key 
