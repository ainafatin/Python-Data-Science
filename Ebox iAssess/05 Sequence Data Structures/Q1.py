# SubSet And SuperSet

# Mohan and Krishna playing Numbers game. Mohan has some certain numbers and Krishna also has some numbers, both are having two sets of numbers.

# Input Formate Specifications:
# The first line of input Contains Set1 integer.
# The second line of Input Contains set2  Integer.

# Output Format Specifications:
# The first line of Output contains set1 is a subset of set2 (True /False ).
# The second line of Output contains set2 is a subset of set1(True /False ).
# The next line of Output contains  set1 is a superset of set2(True /False ).
# The final line of Output contains set2 is a superset of set1(True /False ).
# Sample input and output will be shown below.

# Sample Input  1:
# 1,2,3,4,5,6
# 1,2,3

# Sample Output 1:
# False
# True
# True
# False

set1 = set(input().split(","))
set2 = set(input().split(","))

print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))