# Letter Frequency
# Prakash is the English school teacher at Aksh public school. He wants to teach the English characters to the 1st class students. After taking the class he wanted to know whether his students recognize the letters of English alphabet. So he gave his students a English sentence, and asked them to write down the count of each character in alphabatical order.
 
# Help the students to find the count by writing a program that builds a frequency listing of the characters contained in the file, and prints a sorted and formatted character frequency table to the screen.
 
# Note:
# Read the input from the file and print the output in the console.  
# Input File should be named as frequencyFile.txt.
 
# Input File Content:
# Set of words (or sentences).  
 
# Output Format:  
# Print a sorted and formatted character frequency table. 

# Sample Input and Output: 
# b: 1
# i: 1
# n: 2
# o: 2
# r: 1
# t: 1
# w: 1

file = open("frequencyFile.txt")
words = file.read()

count = {}
for word in words:
    for char in word:
        if char.isalpha():
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
sortedcount = dict(sorted(count.items()))

for char, count in sortedcount.items():
    print(f"{char}: {count}")