# Reshaping Arrays

# Write a Python program to convert a 1-D array to a 2-D array with m rows and n columns.

# Create the 1-D array using the range function by passing 1 parameter that corresponds to the max value.

# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.

# Sample Input and Output :

# Enter the size of 1-D array
# 6
# 1-D Array
# [0 1 2 3 4 5]
# Enter m value
# 3
# Enter n value
# 2
# 2-D Array
# [[0 1]
#  [2 3]
#  [4 5]]

import numpy as np

size = int(input("Enter the size of 1-D array\n"))
arr1 = np.arange(size)

print("1-D Array")
print(arr1)

m = int(input("Enter m value\n"))
n = int(input("Enter n value\n"))
arr2 = arr1.reshape(m, n)

print("2-D Array")
print(arr2)