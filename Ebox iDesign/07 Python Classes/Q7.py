# Student Details

# Veena is a clerk in a college. She keeps the records of all the student details in her system. She is finding it difficult to manage the records manually so she contacts her friend Tina a software Engineer, to help her by writing a code that takes all the student details and displays in the ordered manner. Tina wanted to help Veena but she is not so confident in coding. Help Tina in writing code as required by Veena.   
# Write a program to display the details of the Student by overriding the __str__() Method.

# Create a class named Student with the following private attributes.

# Data Type
# Variable Name

# int
# __id

# str
# __username

# str
# __password

# str
# __name

# str
# __address

# str
# __city

# int
# __pincode

# int
# __contact_number

# str
# __email

# Use __init__() constructor to initialize the attributes with respect to class.

# And this class includes the following member function. 
# No
# Method Name
# Method Description
# 1
# __str__()    
# This method, returns the student details of the current object.

# Input Format:  
# The first input corresponds to the student's id.
# The second input corresponds to the student's username.
# The third input corresponds to the student's password.
# The fourth input corresponds to the student's name.
# The fifth input corresponds to the student's address.
# The sixth input corresponds to the student's city.
# The seventh input corresponds to the student's address Pincode.
# The eighth input corresponds to the student's contact number.
# The ninth input corresponds to the student's email id.

# Output Format:  
# All the user entered details will be displayed one by one(newline).
# The details are printed inside the __str__() method.

# Refer to sample input and output for formatting specifications.
# [All text in bold corresponds to input and the rest corresponds to output.]

# Sample input and output: 
# Enter the student id
# 1
# Enter the  student's username
# nicky
# Enter the password
# nicky
# Enter the name of the student
# nicky
# Enter the address
# nantoor
# Enter the city
# mysuru
# Enter the pincode
# 123456
# Enter the contact number
# 1234567890
# Enter the email id
# nicky@gmail.com

# Id :  1
# User Name :  nicky
# Password :  nicky
# Name :  nicky
# Address :  nantoor
# city :  mysuru
# Pincode :  123456
# Contact Number :  1234567890
# email :  nicky@gmail.com

# Main.py
from Student import Student

u_id = int(input("Enter the student id\n"))
username = input("Enter the student's username\n")
password = input("Enter the password\n")
name = input("Enter the name of the student\n")
address = input("Enter the address\n")
city = input("Enter the city\n")
pincode = int(input("Enter the pincode\n"))
contact_number = int(input("Enter the contact number\n"))
email = input("Enter the email id\n")

student = Student(u_id, username, password, name, address, city, pincode, contact_number, email)
print(student)

# Student.py
class Student:
    def __init__(self,__id,__username,__password,__name,__address,__city,__pincode,__contact_number,__email):
        self.__id = __id
        self.__username = __username
        self.__password = __password
        self.__name = __name
        self.__address = __address
        self.__city = __city
        self.__pincode = __pincode
        self.__contact_number = __contact_number
        self.__email = __email

    def __str__(self):
        return f"Id : {self.__id}\nUser Name : {self.__username}\nPassword : {self.__password}\nName : {self.__name}\nAddress : {self.__address}\ncity : {self.__city}\nPincode : {self.__pincode}\nContact Number : {self.__contact_number}\nemail : {self.__email}"