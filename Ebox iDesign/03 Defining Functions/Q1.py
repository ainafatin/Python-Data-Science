# Default arguments using functions
# Write a python program to get the name of the user and message and display it using functions.
# Function specifications:
# def greet(argument1,argument2 = “Welcome to Python Programming”)

# Input Format:
# Input consists of an string input.
# Output Format:
# Display the statements along with user input.
# Refer to the sample input and output for formatting specifications.
# [All text in bold corresponds to input and the rest corresponds to output.]

# Sample input and Output 1:
# Menu
# 1. Name and Message
# 2. Name
# 1
# Enter the name
# Jack
# Enter the message
# How are you
# Hello Jack, How are you

# Sample input and Output 2:
# Menu
# 1. Name and Message
# 2. Name
# 2
# Enter the name
# Jim
# Hello Jim, Welcome to Python Programming

def greet(argument1, argument2 = "Welcome to Python Programming"):
    return (f"Hello {argument1}, {argument2}")

n = int(input("Menu\n1. Name and Message\n2. Name"))

if (n == 1):
    name = input("Enter the name")
    message = input("Enter the message")
    print(greet(name, message))
elif (n == 2):
    name = input("Enter the name")
    print(greet(name))  