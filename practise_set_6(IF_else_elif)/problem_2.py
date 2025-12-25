#WAP to find out whether a student has passed or failed if it require a total of 40% and at least 33% in each subject to pass. assume 3 subject and take marks as an input from the user.

marks1 = int(input("Enter subject one marks: "))
marks2 = int(input("Enter subject two marks: "))
marks3 = int(input("Enter subject three marks: "))

total_percentage = (marks1+marks2+marks3)/3

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulationn you are clear the exam",total_percentage)
    
else:
    print("Hard luck, try again next year",total_percentage)
