# Module: First Non-Repeating Character

# Sandhya and Pooja are playing string game. And Sandhya gives a string to Pooja, and she has to find a first non-repeating character from that string. So help Pooja by writing a program to find the first non-repeating character from that string.

# Input Format:
# The input consists of a string.

# Output Format:  
# The output consists of a character which represents the first non-repeating character.
# If there is no non-repeating character in the string, then print '#'.

# Note: All text in bold corresponds to input and the rest corresponds to output.

# Sample Input and Output 1:
# swiiss
# w

# Sample Input and output 2:
# naddan
# #

s = input()
charcount = {}
count = 0

for c in s:
    if c in charcount:
        charcount[c] += 1
    else:
        charcount[c] = 1

if all((count > 1 for count in charcount.values())):
    print("#")
else:
    for c in s:
        if (charcount[c] == 1):
            print(c)
            break   