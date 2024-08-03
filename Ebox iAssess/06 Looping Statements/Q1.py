# LIST OF PRIME NUMBERS

# To speed up his composition of generating unpredictable rhythms, A.R.Rahman wants the list of prime numbers available in a range of numbers.
# Can you help him out?
# Write a program to print all prime numbers in the interval [a,b] (a and b, both inclusive).

# Input Format:
# Input consists of 2 integers which correspond to a and b. Assume that a is always less than or equal to b.

# Output Format:
# Refer sample output for details.

# Sample Input 1:
# 2
# 15

# Sample Output 1:
# 2 3 5 7 11 13

a = int(input())
b = int(input())

for num in range(a, b+1):
    if (num > 1):
        isPrime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if (num % divisor == 0):
                isPrime = False
                break
        if isPrime:
            print(num, end=" ")