#WAP find the gratest of three number using the functions


def find_gratest(a , b , c):
    if(a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    
    elif(c>a and c>b):
        return c
    
    else:
        print("you not enter a number")
        
a = 8
b = 10
c = 15
        
print(find_gratest(a , b ,c))
    