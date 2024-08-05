# Mean-Std-Var-1

# Write a python program to find the mean,std and var from pandas dataframe.

# Input Format
# Input is a file in CSV format.

# Output Format
# First line of output refers to mean of the column "pl"
# Second line of output refers to variance of the column "pl"
# Third line of output refers to standard deviation of the column "pl"

# Use 2 precisions for float
# Input File name-"iris.csv"

# Sample Input
# File Input(csv)

# Sample Output

# 5.79 
# 0.64 
# 0.80

import pandas as pd

df = pd.read_csv("iris.csv")

meanvalue = df["pl"].mean()
varvalue = df["pl"].var()
stdvalue = df["pl"].std()

print(f"{meanvalue:.2f}\n{varvalue:.2f}\n{stdvalue:.2f}")