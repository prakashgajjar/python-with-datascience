# To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
username = "     'prakash'    "
print(username.rstrip())

# To ensure that no whitespace exists at the left end of a string, use the lstrip() method.
print(username.lstrip())


# for finding any substring in string
random_string = "yyhe kese ho sub log me hu prakash"
print(random_string.find("su"))
print(random_string.index("s")) #give error if not found the index

print(random_string.count("y")) #find how many time subsring occurence in string

print(random_string.startswith("yyhe")) #return true if that true
print(random_string.endswith("p")) #return true if that true  otehrwise fasle

print(random_string.replace("prakash" , "suthar"))