find = open("hello.txt")
text = find.read()
find.close()
if("twinkless" in text):
    print("yes that exits!")
else:
    print("no that not exits!")