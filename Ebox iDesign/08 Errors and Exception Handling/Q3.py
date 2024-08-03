# P5 / Custom Exception

# Create a class named Student with a single attribute – marks.

# Include a method named check_marks in the Student Class.
# This method checks whether the marks is greater than  or equal to 90 and if it is greater than or equal to 90, the method returns True.

# If the marks is less than 90, a custom Exception named NotEligibleException is raised and an appropriate message as shown in the sample output is displayed.

# Create a custom Exception class named NotEligibleException.

# Create an object of the student class and test the above methods.

# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.

# Sample Input and Output 1:
# Enter marks of student
# 98
# Eligible

# Sample Input and Output 2:
# Enter marks of student
# 56
# Inside Except Block : Not Eligible

class Student:

    def __init__(self, marks):
        self.marks = marks

    def check_marks(self):
        if (self.marks >= 90):
            return True
        else:
            raise NotEligibleException()

class NotEligibleException(Exception):

    def __str__(self):
        return "Inside Except Block : Not Eligible"

try:
    studentmarks = int(input("Enter marks of student\n"))
    student = Student(studentmarks)
    if student.check_marks():
        print("Eligible")
except NotEligibleException as e:
    print(e)