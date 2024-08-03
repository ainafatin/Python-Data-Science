# Symmetric_Difference

# Gokul have two different sets and he wants to find the Symmetric_Difference between two sets. The symmetric difference of two sets A and B is the set of elements that are in either of the sets A or B but not in both.
# So can u please help to write a program to find the symmetric_Difference between two sets.
# Input and Output format will be shown below.

# Input Format Specifications:

# Firstline contains to enter the elements to set1(integers).
# Second-line contains to enter the elements to set2(integers).
# Note that print the elements in sorted order.
# Output Format Specifications:

# Output Consists of Symmetric_difference between set1 and set2 (Integers)
# If both set elements are equal to print ‘invalid set’.
 
# Sample Input1:
# 1,2,3,4,5,6
# 2,3,5,7,8,9
# Sample Output1:
# {1, 4, 6, 7, 8, 9}

# Sample input2:
# 1,2,3
# 1,2,3
# Sample Output2:
# invalid set

input1 = input().split(",")
input2 = input().split(",")

set1 = set(map(int, input1))
set2 = set(map(int, input2))

if ((set1.issuperset(set2)) and (set1.issubset(set2))):
    print("invalid set")
else:
    sd = sorted(set1.symmetric_difference(set2))
    print(f"{{{', '.join(map(str,sd))}}}")