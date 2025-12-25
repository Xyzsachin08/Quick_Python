'''a spam comment is defined as a text contanining following keyword:
"make a lot of money"
"buy now"
"subscribe this"
"click this"
WAP to detect these spams'''

m1 = "make a lot of money"
m2 = "buy now"
m3 = "subscribe this"
m4= "click this"

message = input("Enter a message: ")

if((m1 in message ) or (m2 in message) or (m3 in message) or (m4 in message)):
    print("Message is spam: ")
    
else:
    print("Message is not spam: ")