# Concatenation of Strings
# Fun with “Strings” at Chicago technologies.
# The official heads of chicago technologies thought only working would tire the employees so they arranged some game for relaxation.
# Game 1:
# Rules were as follows:
# • String 1 should define the person and the first letter of the string 1 should be same as the first letter of String 2
# • String 2 should be the person’s name.
# • Output String should be the concatenation of both the input strings.

# Sample Input and Output 1:
# Enter the first string:
# Sleepy
# Enter the second string:
# Subhash
# Sleepy Subhash

# Sample Input and output 2:
# Enter the first string:
# Prem
# Enter the second string:
# Kabir
# Invalid Input

s1 = input("Enter the first string:")
s2 = input("Enter the second string:")
slist1 = list(s1)
slist2 = list(s2)

if (slist1[0] == slist2[0]):
    result = s1 + " " + s2
    print(result)
else:
    print("Invalid Input")   