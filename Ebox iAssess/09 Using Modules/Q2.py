# Module: Continuous Prime Sum
# In Maple Casino, there is a play in which contestant hit a ball to two numbered plates, and then contestant has to say a number which is summation of all the prime numbers from 1 to 'n' , here 'n' represent the first plate number. And the operation will continue upto 't' times, here 't' represent the second plate number.

# Explanation:
# First we perform the sum operation of all the prime numbers from 1 to 7 i.e. {2,3,5,7}, the sum of these prime numbers is: 17.
# Then, again we have to perform the sum of all the prime numbers from 1 to 17, which is the previous sum of prime numbers.
# 1 to 17: {2,3,5,7,11,13,17}, and the resultant sum of prime numbers is: 58.
# This operation will continue upto 2 times (for above mentioned sample input).

# Write a program to find the continous sum of prime numbers 't' times.

# Input Format:
# First line as integer which corresponds to last integer of prime series.
# Second line as integer which corresponds to number of times we have to perform the sum operation of that prime series.

# Output Format:
# A line as integer which corresponds to sum of all the prime numbers.

# Input Format:
# 7
# 2
# Output Format:
# Sum:58

lastint = int(input())
sumop = int(input())

while sumop > 0:
    total = 0
    for n in range(2, lastint + 1):
        for divisor in range(2, n):
            if (n % divisor == 0):
                break
        else:
            total += n
    lastint = total
    sumop -= 1

print(f"Sum:{total}")