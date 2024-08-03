# Second Highest Mark of Student
# You have a record of students. Each record contains the student's name and their marks in Maths, Physics, Chemistry, and computer science. The marks can be floating values. The user enters some integer followed by the names and marks of students. You are required to save the record in a dictionary data type. The user then enters a student's name. The output is the second-highest mark obtained by that student.

# Problem Constraints:
# Use dictionary {} to store the data.
# Use the Dictionary concept to solve the problem.
 
# Input format:
# The first line contains the integer, which indicates the number of students, 'n'.
# The next 'n' lines contain the name and marks obtained by that student separated by a space.
# The final line contains the name of a particular student to find the second-highest mark of him.

# Output format:
# The output is the second-highest mark obtained by the particular student. If he scored the same marks in all subjects, then print a message as shown sample I/O.
# If the student name does not exist then print  "Student doesn't exist". [Refer Sample I/O]

# Sample Input 1:
# 4
# Sandy 78 67 89 100
# John 45 46 48 23
# Cherry 78 78 78 78
# Ratan 78 90 89 56
# Sandy
# Sample Output 1:
# Second Highest mark of Sandy: 89
 
# Sample Input 2:
# 2
# sath 100 100 100 100
# jan 67 56 34 89
# sath
# Sample Output 2:
# sath scored same marks in all subjects: 100

# Sample Input 3:
# 2
# Ratan 78 90 89 56
# Sandy 78 67 89 100
# pooja
# Sample Output 3:
# Student doesn't exist

n = int(input())
d = {}

for i in range(n):
    namemarks = list(input().split())
    name = namemarks[0]
    marks = list(map(int, namemarks[1:4+1]))
    d[name] = marks

name = input()

if name in d:
    marks = d[name]
    if len(set(marks)) == 1:
        print(f"{name} scored same marks in all subjects: {marks[0]}")
    else:
        uniquemarks = list(set(marks))
        uniquemarks = sorted(uniquemarks, reverse=True)
        sec = uniquemarks[1]
        print(f"Second Highest mark of {name}: {sec}")
else:
    print("Student doesn't exist")