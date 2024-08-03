# Ceaser Cipher Encryption

# Ishan playing aa simple game with alphabets. the procedure will be Ishan choose aa random number in between (0-26) and then he changed the alphabets in Ceaser chipper(Each letter 'shifted'  wrt chosen number).
# So can you please help Ishan to write aa program for Ceaser cipher Encryption. Input and Output format Specifications are shown below.

# Input Format Specifications:

# The first line of Input contains a String.
# The next line of input contains Integer N, N is the shifted positions number.
# Replace all characters with the nth character from the current character.
#  Must use "re.sub()".
# Note: [" ord() expected a character, but a string of length 2 found" if the error shows like this then you use the lambda function ].

# Output Format Specifications:

# Output Consists of String.
# if character addition is going greater than 127 then print ‘invalid’.
# Sample Input and Output showed below.
# Sample Input 1:
# amphisoft
# 3
# Sample Output 1:
# dpsklvriw

# Sample Input 2:
# krishnamohan
# 27
# Sample Output 2:
# invalid

import re

s = input()
n = int(input())

pattern = r"."

if any(ord(c) + n > 127 for c in s):
    print("invalid")
else:
    result = re.sub(pattern, lambda match: chr(ord(match.group(0)) + n), s)
    print(result)