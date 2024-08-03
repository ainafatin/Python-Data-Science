# Card Game
# The Westland Game Fair is the premier event of its kind for kids interested in some intellectual and cognitive brain games. Alan, a middle school boy is visiting the fair where he is very much drawn by the Card game.

# The game’s rules are:
# A player needs to pick 3 cards from a big lot of cards. There are 4 types of Cards namely Spade(S), Heart(H), Club(C) and Diamond (D). If all the 3 cards that the player picks are of the same type and same number, they get a Double Bonanza. If all the 3 cards are of the same type or if they all have the same number, they get a Bonanza. Otherwise they do not get a Bonanza. Alan has now picked 3 cards and is awaiting to know if he has got a bonanza. Please help him to know if he has won the Bonanza or not.

# Input Format:
# There are 3 lines of input.
# Each of the line consists of character and integer input, which corresponds to the type of the card and the number in it that Alan picked. The type of card and the number are separated by a single space.

# Output Format:
# Output should display "Double Bonanza" or "Bonanza" or "No Bonanza" based on the conditions given.
# Refer sample input and output for formatting specifications.

# Sample Input 1:
# S 5
# S 5
# S 5

# Sample Output 1:
# Double Bonanza

# Sample Input 2:
# S 6
# S 5
# H 5

# Sample Output 2:
# No Bonanza

# prompt for input (type and number of card seperated by space)
type1, number1 = input().split()
type2, number2 = input().split()
type3, number3 = input().split()

# convert numbers to integer
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

# conditions for cards and print output
if (((type1 == type2) and (type1 == type3)) and ((number1 == number2) and (number1 == number3))):
    print("Double Bonanza")
elif (((type1 == type2) and (type1 == type3)) or ((number1 == number2) and (number1 == number3))):
    print("Bonanza")
else:
    print("No Bonanza")