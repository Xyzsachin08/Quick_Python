#WAP to check the line number

with open("log.txt") as f:
    lines = f.readline()
    
lineno = 1
for line in lines:
    if("Python in line"):
        print(f"Yes python is present. Line no: {lineno}")
        
        
    lineno +=1
    
else:
    print("no python is present")