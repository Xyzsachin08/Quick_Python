#WAP to convert inches to cm


def inch_to_cm(cm):
    return cm/2.54

n = int(input("Enter a number :"))
print(f"The inch is {inch_to_cm(n)}")