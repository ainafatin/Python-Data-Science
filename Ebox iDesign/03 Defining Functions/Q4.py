# Simple Calculator

# Sita was a mathematics teacher and she had to teach the basic mathematic operations to her students. As she was good in programming as well she thought of writing a python program to display all the operations in a single program and perform them choice by choice. Help her with a  code to perform the operations.

# Input and output format:
# Input consists of integer 'n' indicating the choice of operation followed by the integers to perform the chosen operation. The output consists of answer performed according to the choice. Refer sample input and output for better understanding.

# All the texts in bold indicate input and rest indicate output.

# Function Specifications:
# def addition(n1,n2):
# def subtraction(n1,n2):
# def multiplication(n1,n2):
# def division(n1,n2):
# def modulus(n1,n2):

# Sample Input and Output 1:
# Select the operation
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# Enter the choice(1/2/3/4/5):
# 3
# Enter the first number
# 5
# Enter the second number
# 8
# 5 * 8 = 40
 
# Sample Input and Output 2:
# Select the operation
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# Enter the choice(1/2/3/4/5):
# 6
# Invalid Input

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2

print("Select the operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus")
choice = int(input("Enter the choice(1/2/3/4/5):"))

if choice == 1:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"{n1} + {n2} = {(addition(n1,n2))}")
elif choice == 2:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"{n1} - {n2} = {(subtraction(n1,n2))}")
elif choice == 3:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"{n1} * {n2} = {(multiplication(n1,n2))}")
elif choice == 4:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"{n1} / {n2} = {(division(n1,n2))}")
elif choice == 5:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"{n1} % {n2} = {(modulus(n1,n2))}")
else:
    print("Invalid Input")   