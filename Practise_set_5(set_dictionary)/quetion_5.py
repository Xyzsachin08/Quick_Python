'''WAP create an empty dictionary . allow 4 friends to enter their favorite langauage as 
value and use key as their names. assume that the names are unique'''


'''s1 = {}
s1 ["sachin"] = input("Enter favorite langauage: ")
s1 ["bhushan"] = input("Enter favorite langauage: ")
s1 ["onkar"] = input("Enter favorite langauage: ")
s1 ["nisanchu"] = input("Enter favorite langauage: ")
print(s1)'''


#or


d = {}

name = input("Enter friends  name: ")
lang = input("Enter a favorite language: ")
d.update({name:lang})

name = input("Enter friends  name: ")
lang = input("Enter a favorite language: ")
d.update({name:lang})

name = input("Enter friends  name: ")
lang = input("Enter a favorite language: ")
d.update({name:lang})

name = input("Enter friends  name: ")
lang = input("Enter a favorite language: ")
d.update({name:lang})

print(d)