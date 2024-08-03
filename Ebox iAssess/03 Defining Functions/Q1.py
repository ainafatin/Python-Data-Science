# Multiple 2 numbers using default arguments
 
# Write a program to multiple two values using default arguments.

# Suppose the 2 input values are a and b.

# Make 3 function calls as follows:
# 1) multiply(a)
# 2) multiply(a,b)
# 3) multiply(a,b=9)

# Functional Specifications:
# def multiply(argument1,argument2=10):

# Input Format:
# Input consists of 2 integers.

# Output Format:
# Output prints the product of the given input.

# Sample Input  and Output:
# 5
# 3
# The result is 50
# The result is 15
# The result is 45

def multiply(argument1, argument2 = 10):
    return argument1 * argument2

a = int(input())
b = int(input())
print(f"The result is {multiply(a)}")
print(f"The result is {multiply(a, b)}")
print(f"The result is {multiply(a, 9)}")