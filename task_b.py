grade = input('Enter numerical grade between 0-100: ')
if (grade.isnumeric()):
    grade = int(grade)
    if grade >= 80 and grade <= 100:
        print("Your grade is: A") 
    elif grade <= 79 and grade >= 60:
        print("Your grade is: B")
    elif grade >= 50 and grade <= 59:
        print("Your grade is: C")
    elif grade >= 40 and grade <= 49:
        print("Your grade is: D")
    elif grade >= 0 and grade <= 39:
        print("Your grade is: F")
else:
    print("Error: Please enter a number")
    