f = open("file.txt")

print(f.read())

f.close()


#the same can be written using with statement
with open("file.text"):
    print(f.read())
    
    #don't need close