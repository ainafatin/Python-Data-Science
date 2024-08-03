# CSV write

# Saahil is working as a Receptionist at ABC Engineering College. The CSE department is conducting interview for the post of Asst. Professor. He was asked to note down the salary expectation of all the interviewees. Due to some error with MS Excel software and he is not able to write the details in the CSV format. So help him by writing a program that would write the given data to a file, and finally print the file content.

# Note :
# Read the input from the console and write the output to a file.

# The name of the output file should be "salaryData.csv".

# Input Format:
# First Line is an integer corresponding to 'n' the number of persons.
# next n*2 lines corresponds to each persons name and salary.

# Sample Input:
# 4
# nisha
# 30000
# karthikeyan
# 40000
# krishna
# 30000
# shakthi
# 35000

# Output File Format:
# nisha,30000
# karthikeyan,40000
# krishna,30000
# shakthi,35000

n = int(input())

details = []
while n > 0:
    name = input()
    salary = int(input())
    details.append([name, salary])
    n -= 1

file = open("salaryData.csv", "w")

for detail in details:
    file.write(f"{detail[0]},{detail[1]}\n")