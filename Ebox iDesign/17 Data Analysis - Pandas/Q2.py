# Import CSV file as DF

# Write a Python program to import the given CSV file as a Pandas Data Frame.

# The input file to be used is iris.csv file. Note that there is no header row in the input file.

# The input file is given as part of the template code.

import pandas as pd

data = pd.read_csv("iris.csv", names=["sepal_length","sepal_width","petal_length","petal_width","species_type"], header=0)

print(data)