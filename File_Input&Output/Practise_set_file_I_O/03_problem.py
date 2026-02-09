'''
WAP to genrate multiplication tables from 2 to 20 an write it to the 
diffrent files. place these files ina folder for a 13 - year old
'''


def genrateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"
        
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    genrateTable(i)