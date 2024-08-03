# Class with Public Attributes

# Create a class named Person with the following 2 public attributes.
# name
# age

# Include a constructor:
# __init__(self,name, age)

# Create an object of class Person to test the above class.

# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.

# Sample Input and Output:
# [All text in bold corresponds to input and the rest corresponds to output]
# Enter name
# Mahirl
# Enter age
# 10
# Person Details
# Mahirl
# 10

# Main.py
from Person import Person

name = input("Enter name\n")
age = int(input("Enter age\n"))

person = Person(name, age)
print(person)

# Person.py
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person Details\n{self.name}\n{self.age}"