# Exploring Exponential and Trigonometric Functions with SciPy

# Write a Python program to explore the functionalities of SciPy's Special Function package. Write a program to demonstrate the usage of various exponential and trigonometric functions available in SciPy, Use exp10(), sindg(), and cosdg().

# Input and Output format:
# The first line of input contains the exponent value for exponent calculation. 
# The second line of input contains the angle in degrees for sine and cosine calculation. 

# Sample Input and Output:
# Enter the exponent value:
# 3
# 10 raised to the power of 3 : 1000.0
# Enter the angle in degrees:
# 90
# Sine of 90.0 degrees: 1.0
# Cosine of 90.0 degrees: -0.0

import scipy.special as sp

e = int(input("Enter the exponent value:"))

print(f"10 raised to the power of {e} : {sp.exp10(e)}")

a = int(input("Enter the angle in degrees:"))

print(f"Sine of {a:.1f} degrees: {sp.sindg(a)}")
print(f"Cosine of {a:.1f} degrees: {sp.cosdg(a)}")