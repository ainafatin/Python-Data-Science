# Type Error Exception
# Saurav is coach of ABC school cricket team. His team captain not performing well from last few matches. So, coach wants to find the batting average of his captain.
# Thus, write a program to find the batting average of his captain, for given 'n' matches.

# This program may generate Type Error exception, if there is a type mismatch when rating is got as input. Use exception handling mechanisms to handle this exception. 
  
# Input and Output Format: 
# Refer sample input and output for formatting specifications.
# Batting average should be rounded off to two decimal places.

# Note: All text in bold corresponds to input and the rest corresponds to output. 
  
# Sample Input and Output 1: 
# Enter the number of matches
# 4 
# Enter the scores
# 34
# 12
# 24
# 20
# Batting average: 22.50

# Sample Input and Output 2: 
# Enter the number of matches
# 2 
# Enter the scores
# 10
# r 
# Type Error Exception

try:
    n = int(input("Enter the number of matches\n"))

    scores = []
    print("Enter the scores")

    for i in range(n):
        scores.append(int(input()))
    average = sum(scores) / len(scores)
    print(f"Batting average: {average:.2f}")

except ValueError:
    print("Type Error Exception")