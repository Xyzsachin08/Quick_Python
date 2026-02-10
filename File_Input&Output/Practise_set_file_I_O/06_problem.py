#WAP to mine a log file and finnd out whether it contains 'python'.

with open("log.txt") as f:
    content = f.read()
    
if ("python" in content):
    print("Yes python is present")
else:
    print("No python is not present")