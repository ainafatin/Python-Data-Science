# P3 / POSITIVE NUMBERS

# Write a program that prompts users to enter numbers till he enters one positive number. Whenever the user enters a negative number or a string , raise a ValueError exception and handle it appropriately and display the message shown in the sample output.

# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.

# Sample Input and Output 1:
# Enter a positive integer
# 5
# Good! You entered 5

# Sample Input and Output 2:
# Enter a positive integer
# -6
# You entered a negative number. Retry!
# Enter a positive integer
# -9
# You entered a negative number. Retry!
# Enter a positive integer
# 3
# Good! You entered 3

class PositiveNumber:

    def __init__(self, num):
        self.num = num

    def check_number(self):
        if (self.num > 0):
            return True
        else:
            raise ValueError()

class ValueError(Exception):

    def __str__(self):
        return "You entered a negative number. Retry!"

n = -1
while n <= 0:
    try:
        n = int(input("Enter a positive integer\n"))
        num = PositiveNumber(n)
        if num.check_number():
            print(f"Good! You entered {n}")
    except ValueError as e:
        print(e)