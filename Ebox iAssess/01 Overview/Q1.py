# WonderWorks Magic Show
# The Magic Castle, the home of the Academy of Magical Arts at California has organized the great ‘WonderWorks Magic Show’. 3 renowned magicians were invited to mystify and thrill the crowd with their world’s spectacular magic tricks. At the end of each of the 3 magicians’ shows, the audience were requested to give their feedback in a scale of 1 to 10. Number of people who watched each show and the average feedback rating of each show is known. Write a program to find the average feedback rating of the WonderWorks Magic show.

# Input Format:
# First line of the input is an integer value that corresponds to the number of people who watched show 1.
# Second line of the input is a float value that corresponds to the average rating of show 1.
# Third line of the input is an integer value that corresponds to the number of people who watched show 2.
# Fourth line of the input is a float value that corresponds to the average rating of show 2.
# Fifth line of the input is an integer value that corresponds to the number of people who watched show 3.
# Sixth line of the input is a float value that corresponds to the average rating of show 3.

# Output Format:
# Output should display the overall average rating for the show. Display the rating correct to 2 decimal places.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output:
# Enter the number of people who watched show 1
# 400
# Enter the average rating for show 1
# 9.8
# Enter the number of people who watched show 2
# 500
# Enter the average rating for show 2
# 9.6
# Enter the number of people who watched show 3
# 100
# Enter the average rating for show 3
# 5
# The overall average rating for the show is 9.22

# input
show1 = int(input("Enter the number of people who watched show 1"))
rating1 = float(input("Enter the average rating for show 1"))
show2 = int(input("Enter the number of people who watched show 2"))
rating2 = float(input("Enter the average rating for show 2"))
show3 = int(input("Enter the number of people who watched show 3"))
rating3 = float(input("Enter the average rating for show 3"))

# calculation
rating = (show1 * rating1) + (show2 * rating2) + (show3 * rating3)
total = show1 + show2 + show3
averagerating = rating / total

# output
print(f"The overall average rating for the show is {averagerating:.2f}")