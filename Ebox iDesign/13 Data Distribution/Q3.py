# Mean-Std-Var-2

# Write a python program to find the mean,std and var from pandas dataframe.

# Input Format
# Input is a file in CSV format.

# Output Format
# First line of output refers to mean of the column "cyl"
# Second line of output refers to variance of the column "cyl"
# Third line of output refers to standard deviation of the column "cyl"

# Use 2 precisions for float
# Input File name-"cars.csv"

# Sample Input
# File Input(csv)

# Sample Output

# 6.50
# 2.40
# 1.55

import pandas as pd

df = pd.read_csv("cars.csv")

meanvalue = df["cyl"].mean()
varvalue = df["cyl"].var()
stdvalue = df["cyl"].std()

print(f"{meanvalue:.2f}\n{varvalue:.2f}\n{stdvalue:.2f}")