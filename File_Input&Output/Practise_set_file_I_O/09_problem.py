with open("file1.txt")as f:
    content1 = f.read()
    
with open("file.txt")as f:
    content2 = f.read()
    
if(content1 == content2):
    print("Yes files are identical")
    
else:
    print("No these files are not indentical")