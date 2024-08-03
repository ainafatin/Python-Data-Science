# Displaying user inputs using multiple return values
# Write a program to display the user entered details and return multiple values.
# Functions Sepcifications:
# def multiVarFunc()

# Input Format:
# First line of input consists of String which is department name.
# Second line of input consists of integer input which is the total number of students
# Third line of input consists of integer input which is the total number of faculty.

# Output Format:
# Display the user inputs.

# Sample Input and Output:
# Enter department name:
# CSE
# Enter the number of total students:
# 60
# Enter the number of total faculties:
# 15
# Details:
# Department:CSE
# Total students:60
# Total faculties:15

def multiVarFunc(dept, students, faculties):
    print(f"Department:{dept}")
    print(f"Total students:{students}")
    print(f"Total faculties:{faculties}")

deptname = input("Enter department name:\n")
noofstudents = int(input("Enter the number of total students:\n"))
nooffaculty = int(input("Enter the number of total faculties:\n"))

print("Details:")
multiVarFunc(deptname, noofstudents, nooffaculty)