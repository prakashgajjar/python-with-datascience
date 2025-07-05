import os 

if (os.path.exists("test")):
    print("folder already exists")
else:
    os.mkdir("test")
    
    print("folder created")
    
listname = os.listdir("../basic")
print(listname)

print(os.getcwd())

os.rename('test' , 'test1')
os.rename('test1' , 'test')

data =  os.stat('main.py')
print(data)