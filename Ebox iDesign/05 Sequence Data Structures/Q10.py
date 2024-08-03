# Word Count
# Harry studies in HNJ school and his medium of instruction is English. His English teacher taught him to form sentences. Harry loves Mathematics as well. He wants to link Mathematics with English. As a first step, he wishes to count the number of occurrences of words in a sentence.

# Develop a python program to help Harry to finish the task.

# Input Format:
# Read a sentence from the user

# Output Format:
# Display the number of occurrences of words in the sentence. 

# Refer sample output.

# Sample Input 1:
# the the function using dict dict

# Sample Output 1:
# {'the': 2, 'function': 1, 'using': 1, 'dict': 2}

s = input().split()
d = {}
count = 0

for word in s:
    if word in d:
        count = d[word]
    else:
        count = 0
    count += 1
    d[word] = count

print(d)   