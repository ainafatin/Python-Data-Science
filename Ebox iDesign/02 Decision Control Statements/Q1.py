# Lucky Winner
# It was the inaugural ceremony of "Fantasy Kingdom" Amusement park and the park Management has announced some lucky prizes for the visitors on the first day. Based on this, the visitors whose ticket number has the last digit as 3 or 8, are declared as lucky winners and attracting prizes are awaiting to be presented for them.
# Write a program to find if the last digit of the ticket number of visitors is 3 or 8.

 
# Input Format:
# First line of the input is an integer that corresponds to the ticket number.

# Output Format:
# Output should display as "Lucky Winner" if the last digit of the ticket number is 3 or 8. Otherwise print "Not a Lucky Winner".
# Refer sample input and output for formatting specifications.

# Sample Input 1:
# 43

# Sample Output 1:
# Lucky Winner

# Sample Input 2:
# 41

# Sample Output 2:
# Not a Lucky Winner

ticketno = int(input())

if ((ticketno % 10 == 3) or (ticketno % 10 == 8)):
    print("Lucky Winner")
else:
    print("Not a Lucky Winner")