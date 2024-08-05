# Maximum and Minimum Turnovers
 
# Ramesh is self-employed. it's been years after setting his business. With all the hardships he brought his business into the track. He got a thought to analyze his graph of progress from last year to the current year.  
# He has a list of data containing the transactions done per month in a year, he wanted to calculate the turnovers of the month and which month had the Maximum turnover and which month had the minimum turnover.

# But unaware of any software he had to do it manually which was tedious work.  He asks Suresh, a Software Engineer to help him in this. Fortunately, Suresh was working on data science and thought he could easily help him. 
# Assume yourself to be in Suresh's position and had to help Ramesh in tracking his growth from last year to current year. Given the data set of calculate the turnovers of the month and which month had the Maximum turnover and which month had the minimum turnover.

# Note: All positive values in the transactions are considered as the "Income" and All negative values are considered as "Investment".

# Input Format:
# Input consists of an array indicating the transactions done over the year.

# Output Format:
# The Output displays the months having the maximum turnover and the minimum turnover.

# Refer sample input and output for formatting specifications.

# Sample Input and Output: 

# Enter the transaction done last year
# 10000
# 7898
# 7878
# 787878
# 787878
# 777
# 777878
# 77777
# -5656556
# 45454
# 45455
# 4545454
# Minimum Turnover : -5656556
# Maximum Turnover : 4545454
# Minimum Turnover Month : 8
# Maximum Turnover Month : 11

import numpy as np

inputlist = []
print("Enter the transaction done last year")
for i in range(12):
    userinput = int(input())
    inputlist.append(userinput)
inputarray = np.array(inputlist)

minvalue = np.min(inputarray)
maxvalue = np.max(inputarray)

minindex = np.argmin(inputarray)
maxindex = np.argmax(inputarray)

print(f"Minimum Turnover : {minvalue}")
print(f"Maximum Turnover : {maxvalue}")
print(f"Minimum Turnover Month : {minindex}")
print(f"Maximum Turnover Month : {maxindex}")