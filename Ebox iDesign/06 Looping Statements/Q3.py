# Series
# The Event Organizing Company "Buzzcraft" focuses event management in a way that creates a win-win situation for all involved stakeholders. Buzzcraft don't look at building one time associations with clients, instead, aim at creating long-lasting collaborations that will span years to come. This goal of the company has helped them evolve and expand big with organizing many events till date.
# The number of events that the company organizes every month is recorded sensibly and is seemed to have followed a specific series like: 30, 35, 38, 41, 54, 53 ...

# Write a program which takes an integer N as the input and will output the series till the Nth term.

# Input Format:
# First line of the input is an integer N.

# Output Format:
# Output a single line the series till Nth term, each separated by a comma.
# Refer sample input and output for formatting specifications.

# Sample Input 1:
# 5

# Sample Output 1:
# 30 35 38 41 54

# Sample Input 2:
# 10

# Sample Output 2:
# 30 35 38 41 54 53 78 71 110 95

# prompt input for N denoting the Nth term for the number series
N = int(input())

# initialize a number list starting from 30 and 35
numlist = [30, 35]

# initial difference
even = 6
odd = 8

# index for list
x = 0
y = 1

# using for loop
if (N >= 2):
    for i in range(1, N):
        if (i % 2 == 0):
            nextnum = numlist[y] + even
            even += 6
            y += 2
        else:
            nextnum = numlist[x] + odd
            odd += 8
            x += 2
        if (len(numlist) < N):
            numlist.append(nextnum)
elif (N == 1):
    numlist = [30]
else:
    numlist =[]

# print results
for num in numlist:
    print(num, end=" ")