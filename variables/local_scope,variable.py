#scope:= Scope = where a variable can be used
       #types of scope:= 1.local scope
                        #2.global scope
                        #3.nonlocal scope
                        
                        
#Local Scope: Variable inside function,accesible for only inside function

def show():
    x = 10   # local variable
    print(x)

show()