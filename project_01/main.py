'''
project 01 = snake water gun game

we all have played snake , water gun game in our childhood. if you haven't , google
the rules of this game and write a python program capable of playing this game with the 
user.

'''

import random


computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "Snake", -1: "water", 0: "Gun"}

you = youDict[youstr]

print(f"you choice{reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if(computer == you):
    print("it's a draw")
    
else:
    if(computer == -1 and you ==1):
        print("you win!")
        
        
    elif(computer == -1 and you ==0):
        print("you lose")
        
    elif(computer == 1 and you == -1):
        print("you lose")
        
    elif(computer == 0 and you == -1):
        print("you win")
        
    elif(computer == 0 and you ==1):
        print("you lose")
        
    else:
        print("Something went wrong!")
    
