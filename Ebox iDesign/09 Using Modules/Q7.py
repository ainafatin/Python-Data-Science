# Write a program to calculate maximum and minimum number from the given user input.
# Note : Use built-in function only.

# Input and Output Format :
# (Refer sample input and output)
# [All text in bold corresponds to input and rest others are output]

# Sample Input and Output :
# Enter the values:
# 1 4 6 12 73 92 134
# The maximum value is : 134
# The minimum value is : 1

print("Enter the values:")
numbers = input().split(" ")
numbers = [int(number) for number in numbers]

maximum = max(numbers)
minimum = min(numbers)

print("The maximum value is :", maximum)
print("The minimum value is :", minimum)