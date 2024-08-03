# Password Extraction

# Ebox Engineering college has lot of systems in various labs and libraries. Each system in college running with windows OS having different username with different passwords . Student can choose any non admin user from the system and have to extract password from the given hint. Password is always a number of any length or no password . From the hint given , user has to extract the maximum number and that extracted number will be used as password. If no number present in the hint then there is no password for that particular system user.
# Help the students to find the password by writing a program.

# Input and Output Format:
# Input is single line string which is a hint. String contains only alphanumeric characters.
# Output is a maximum number extracted from the input string.consider only positive numbers.print “No Password” without quotes when input has no number.
# Refer sample input and output for formatting specifications

# Sample Input 1:
# hello123 abcd456 efgh99999
# Sample Output 1:
# 99999

# Sample Input 2:
# abcdefgh
# Sample Output 2:
# No Password

import re

s = input()
p = r"\d+"
numlist = re.findall(p, s)

if not numlist:
    print("No Password")
else:
    numlist = [int(num) for num in numlist]
    maximum = max(numlist)
    print(maximum)