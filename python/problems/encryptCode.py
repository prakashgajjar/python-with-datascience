#encrypt the code like if word contain more then 3 char remove forst latter and append in last and add 3 random char in satrting and ending 
import random 

def encypt(word):
    str1 = "abcdefghijklmnopqrstuvwxyz"
    if(len(word) < 3):
        reversed = word[::-1]
        return reversed
    else:
        reversedWord = word[1:] + word[0]
        prefix = "".join(random.choices(str1 , k = 3))
        postfix = "".join(random.choices(str1 , k = 3))
        return prefix + reversedWord + postfix

def decode(word):
    if(len(word) < 3):
        orgWord = word[::-1]
        return orgWord
    else:
        reversedWord = word[3:-3]
        orgWord = reversedWord[-1] + reversedWord[0:-1]
        return orgWord

    
print(decode("biarakashpwmu"))


# print(aorgWord)







