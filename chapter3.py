'''#Strings
a = "sachin"
b = """sachin"""


# string is a immutable , you cant't modify and update any string
name = "xyzsachin"
nameshort = name[0:3]#string slicing
print(nameshort)


#Negative slicing
sachin = "borudesachin"
print(sachin[-4:-1])
print(sachin[1:5:3])
 
 
#String function
n = "princess"
print(len(n))
print(n.endswith("cess"))
print(n.startswith("prin"))
print(n.capitalize())
print(n.lower())
print(n.upper())
print(n.title())


#Escape seqvence characters
h = "Good morning all of you \n today i am here to tell something about my life"
print(h)'''


#Quetion_1 WAP python program to display a user entered name followed by good afternoon using input() function.
'''a = input("Enter a name: ")
print(f"Good Afternoon {a}")'''


#WAP to fill in a letter template given below with name and date.
letter = '''Dear\t<|Name|>,
            you are selected! 
            <|Date|>'''
            
print(letter.replace("<|Name|>","Harry").replace("<|Date|","24 september 2050"))




