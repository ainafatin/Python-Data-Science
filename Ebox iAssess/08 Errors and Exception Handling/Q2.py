# CustomException: Invalid Password Exception
# Vicky's father wants to create the whatsApp account. But again and again Invalid Password error comes. So Vicky helps his father to create a account. During account creation he has enter the username and password, in which the password should be contain atleast one lowercase letter, one upper case letter and a number, otherwise exception occured.
# So write a program to check the password is valid or invalid.

# Note:
# Conditions for a valid password: 
# Password should contain atleast one lowercase letter, one upper case letter and a number. 
# Use exception handling mechanisms to handle these exceptions 
 
# Input and Output Format: 
# Refer sample input and output for formatting specifications. 
# All text in bold corresponds to input and the rest corresponds to output. 

# Sample Input and Output 1 : 
# Enter the username
# Vikram
# Enter the password 
# 1samudrA
# Employee Username: Vikram
# Password: 1samudrA

# Sample Input and Output 2 : 
# Enter the username 
# Rashmi
# Enter the password 
# hawai
# CustomException: Invalid Password Exception

class CustomException(Exception):
    def __init__(self, message="CustomException: Invalid Password Exception"):
        self.message = message
        super().__init__(self.message)

lower = 0
upper = 0
num = 0

try:
    username = input("Enter the username\n")
    password = input("Enter the password\n")
    for c in password:
        if (c.islower()):
            lower += 1
        elif (c.isupper()):
            upper += 1
        elif (c.isnumeric()):
            num += 1
    if (lower > 0) and (upper > 0) and (num > 0):
        print(f"Employee Username: {username}\nPassword: {password}")
    else:
        raise CustomException()
except CustomException as e:
    print(e)