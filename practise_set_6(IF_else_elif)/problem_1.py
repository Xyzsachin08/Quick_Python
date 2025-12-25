#WAP to find the greatest of four numbers entered by the user

a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
c = int(input("Enter a number 3: "))
d = int(input("Enter a number 4: "))

if(a>b and a>c and a>d):
    print("A is largest no:",a)
elif(b>a and b>c and b>d):
    print("b is largest no:",b)
elif(c>a and c>b and c>d):
    print("c is largest no:",c)
elif(d>a and d>b and d>c):
    print("d is largest no:",d)

    
