# Tile Game
# In connection to the National Mathematics Day celebration, the Regional Mathematical Scholars Society had arranged for a Mathematics Challenge Event where school kids participated in large number. Many interesting math games were conducted, one such game that attracted most kids was the tile game where the kids were given 'n' square tiles of the same size and were asked to form the largest possible square using those tiles.

# Help the kids by writing a program to find the area of the largest possible square that can be formed, given the side of a square tile (in cms) and the number of square tiles available.

# Input Format:
# First line of the input is an integer that corresponds to the side of a square tile (in cms).
# Second line of the input is an integer that corresponds to the number of square tiles available.

# Output Format:
# Output should display the area of the largest possible square that can be formed (in square cms) with the available tiles.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output :
# Enter the side in cm of a square tile
# 5
# Enter the number of square tiles available
# 8
# Area of the largest possible square is 100sqcm

# input
side = int(input("Enter the side in cm of a square tile"))
tile = int(input("Enter the number of square tiles available"))

# largest possible square
largest_square = int(tile ** 0.5)

# largest side length of largest possible square
largest_side = largest_square * side

# largest area using largest side length
largest_area = largest_side * largest_side

# output
print(f"Area of the largest possible square is {largest_area}sqcm")