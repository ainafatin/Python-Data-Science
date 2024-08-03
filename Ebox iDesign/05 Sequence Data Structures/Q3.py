# Pattern Printing

# It was a fun week in Rita's college.Many competitions were organized for the students.Rita was very interested in pattern printing competition. She was given an integer indicating a number of '\' or'/' she had to print in the given pattern. 

# Though she was good in it she is finding it difficult to print the given pattern. Help Rita by writing a python code for the given input specifications.

# /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\

# Input and output format:
# Input consists of an integer indicating a number of ‘/’ and ‘\’ Output consists of the pattern with specified number of backward and forward slashes.

# All the texts in bold refer Input and rest refer output.
# Sample Input:
# 5
# Sample Output:
# /////\\\\\/////\\\\\
# /////\\\\\//////\\\\\
# /////\\\\\/////\\\\\
# /////\\\\\//////\\\\\
 
# Sample Input:
# 10
# Sample Output:
# //////////\\\\\\\\\\//////////\\\\\\\\\\
# //////////\\\\\\\\\\//////////\\\\\\\\\\
# //////////\\\\\\\\\\//////////\\\\\\\\\\
# //////////\\\\\\\\\\//////////\\\\\\\\\\

n = int(input())

for row in range(4):
    print("/" * n + "\\" * n + "/" * n + "\\" * n)