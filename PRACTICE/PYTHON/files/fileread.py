file =open("hello.txt" , "w")
file2 = open('hello2.txt', 'r')

file.write(file2.read())