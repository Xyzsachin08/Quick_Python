#Nonlocal Scope:=  Used in nested function

def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)

outer()  #output is 20 means changes value of outer function