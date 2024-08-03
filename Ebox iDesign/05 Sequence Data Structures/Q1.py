# Character Deletion in a String
# Sita and Gita were no so good friends and had a fight while doing tasks so one of them decided to teach a lesson to other and deleted one of the characters from her name entered in the company’s database.

# Input format:
# First line of the Input is a string indicating the name.
# Second line of the input is an integer ‘n’( a value less than the string length).
# Output Format:
# The output contains a string with a character being deleted at ‘nth’ index of the input.
# Sample input 1:
# Andrews
# 2
# Sample output 1:
# Adrews
# Sample input 2:
# Jack
# 4
# Sample output 2:
# Jac

name = input()
n = int(input())

c_name = []
for c in name:
    c_name.append(c)

del c_name[n-1]

for name in c_name:
    print(name, end="")