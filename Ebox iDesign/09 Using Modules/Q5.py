# Module: GCD of Two Numbers

# The greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. After the explanation given by tuition teacher, now he wants to conduct the small test to check their understanding of GCD concept.
# So, help the students by writing a program to find the GCD of Two Numbers.

# Input  Format: 
# The input consists of two integers.

# Output  Format:
# The output consists GCD of Two Numbers.

# Note: All text in bold corresponds to input and the rest corresponds to output.

# Sample Input and Output:
# Enter the two positive numbers
# 12
# 14
# GCD:2

def GCD(n1, n2):
    if n1 == n2:
        return n1
    elif n1 > n2:
        return GCD(n1-n2, n2)
    else:
        return GCD(n1, n2-n1)

print("Enter the two positive numbers")
n1 = int(input())
n2 = int(input())

print(f"GCD:{GCD(n1,n2)}")   