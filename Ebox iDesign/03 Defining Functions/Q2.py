# Leap year using default arguments
 
# Write a program to find leap year using default arguments.

# Functional Specifications:
# def daysInYear(argument1,argument2=False)

# Input Format:

# Input consists of a year.

# Output Format:
# Output prints the whether the given year is leap year or not.

# Sample Input  and Output:
# 2000
# 2000 is a leap year

def daysInYear(argument1, argument2=False):
    if ((argument1 % 4 == 0) or ((argument1 % 400 == 0) and (argument1 % 100 != 0))):
        argument2 = True
        return (f"{argument1} is a leap year")
    else:
        return (f"{argument1} is not a leap year")

year = int(input())
print(daysInYear(year))