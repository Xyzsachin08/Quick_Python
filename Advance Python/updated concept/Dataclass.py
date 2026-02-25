from dataclasses import dataclass

@dataclass
class User:
    name:str
    age:int

u=User("Sachin",19)
print(u)