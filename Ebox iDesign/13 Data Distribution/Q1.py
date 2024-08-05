# Chebyshev distance - Similarity

# In this problem, given two feature vectors as input , find the Chebyshev distance between the given vectors without using any inbuild python libraries.

# Input format :
# 1st line of input is an integer ‘n’, which corresponds to the length of both the vectors
# Next 2 lines of input consists of ‘n’ space separated integers, which corresponds to the 1st and 2nd input vectors .

# Output Format :
# Output corresponds to single integer value, which corresponds to the Chebyshev Distance between the vectors.

# Note : print ‘Invalid Input’ , if the vectors length doesn’t match.

# Sample Input :
# Enter the length of the array
# 3
# 1 5 89
# 236 4 58

# Sample Output :
# 235

print("Enter the length of the array")
n = int(input())

v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

if len(v1) != n or len(v2) != n or len(v1) != len(v2):
    print("Invalid Input")
else:
    maxdiff = 0
    for i in range(n):
        diff = abs(v1[i] - v2[i])
        if diff > maxdiff:
            maxdiff = diff
    print(maxdiff)