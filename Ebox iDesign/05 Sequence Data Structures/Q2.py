# Print Palindrome

# James and Jones had a discussion on palindrome strings. They were assigned to a task in which they had to check if the given string is a palindrome or not and if not they had to make it as a palindrome.
# The condition for the task was as follows:
# • Input and output strings should be case sensitive.
# Help them with a program to make their task easier.

# Input format:
# Input consists of a string.
# output format:
# the output will be a palindrome string.
# Sample Input:
# Tamil
# Sample Output
# TamaT

# Sample Input:
# Amphi
# Sample Output
# AmpmA

# input
inputstring = input()
inputlist = list(inputstring)

# initialize variables
palindrome = []
mid = (len(inputstring)) // 2

# assign to list until the middle of the string
if (len(inputstring) % 2 == 0):
    for i in range(0, mid):
        palindrome.append(inputlist[i])
else:
    for i in range(0,mid+1):
        palindrome.append(inputlist[i])

# reverse the remaining string
for i in range(mid-1, -1, -1):
    palindrome.append(inputlist[i])

# output
for p in palindrome:
    print(p, end="")   