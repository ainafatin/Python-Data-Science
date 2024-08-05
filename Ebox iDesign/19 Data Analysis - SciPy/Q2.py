# Calculating the Mean of User-Inputted Numbers

# Write a Python script that prompts the user to enter a list of numbers separated by spaces. Your script should then calculate and print the mean (average) of these numbers. Ensure your code handles both integer and floating-point inputs.

# The script first prompts the user to input the values of the independent variable (x) and dependent variable (y) separated by spaces.

# Then converts these input strings into arrays of floating-point numbers using list comprehensions and the split() method.

# Using the linregress() function from scipy.stats, the script performs linear regression on the input data, returning the slope, intercept, correlation coefficient (r-value), p-value, and standard error of the regression coefficients.

# Prints out these statistical results, including the slope, intercept, R-squared value (squared correlation coefficient), p-value (probability of observing the data given that the null hypothesis is true), and standard error of the regression coefficients.

# Sample input & output 1:

# Enter the values of x separated by spaces: 1 2 3 4 5
# Enter the values of y separated by spaces: 2 3 5 4 6
# Slope: 0.9
# Intercept: 1.2999999999999998
# R-squared: 0.81
# p-value: 0.03738607346849863
# Standard error: 0.25166114784235827

# Sample input & output 2:

# Enter the values of x separated by spaces: -1 0 1 2 3
# Enter the values of y separated by spaces: -3 -1 1 3 5
# Slope: 2.0
# Intercept: -1.0
# R-squared: 1.0
# p-value: 1.2004217548761408e-30
# Standard error: 0.0

import scipy.stats as sp

x = input("Enter the values of x separated by spaces:")
x = [float(value) for value in x.split()]

y = input("Enter the values of y separated by spaces:")
y = [float(value) for value in y.split()]

slope, intercept, rvalue, pvalue, stderror = sp.linregress(x, y)
rsquared = rvalue ** 2

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", rsquared)
print("p-value:", pvalue)
print("Standard error:", stderror)