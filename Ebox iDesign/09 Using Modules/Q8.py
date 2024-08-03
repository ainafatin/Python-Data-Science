# Write a program to find the character based on the ASCII value given by the user as an input. Display the character based on the ascii value provided by the user.

# Note : Refer to the problem requirements

# Input and Output Format :
# (Refer to sample input and Output)
# [All text in bold corresponds to input and rest others are output]

# Sample Input and Output :
# Enter the value :
# 65
# Character of ASCII value 65 is  A

num = int(input("Enter the value :\n"))
asciivalue = ""

for n in [num]:
    asciivalue += chr(n) 

print(f"Character of ASCII value {num} is  {asciivalue}")   