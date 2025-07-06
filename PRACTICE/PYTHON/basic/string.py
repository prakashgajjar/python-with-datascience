# all about string 

name = 'suthar prakash'

#title use for capitalize the first latter of evry word that not chnage the string string is unmutable
print(name.title()) 

#for convert to whole string into upercase and lowercase we use 
print(name.upper()) 
print(name.lower()) 

#Combining or Concatenating Strings
first_name = "suthar"
last_name  = "prakash"

full_name = first_name + last_name
print(full_name)

#you can write one string and variable that contain string only string 
full_name1 = "prakash" + last_name
print(full_name1)

# Adding Whitespace to Strings with Tabs or Newlines

# To add a tab to your text, use the character combination \t as shown at
print('\tprakash suthar')

#To add a newline in a string, use the character combination \n
print('\nprakash suthar')

#You can also combine tabs and newlines in a single string
print('\n\tprakash suthar')