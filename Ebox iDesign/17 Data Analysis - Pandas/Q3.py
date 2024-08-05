# Import Specific Columns from CSV file as DF

# Write a Python program to import specific columns from a given CSV file as a Pandas Data Frame.

# The 2 columns to be imported are sepal_length and sepal_width.

# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

# The input file is given as part of the template code.

import pandas as pd

df = pd.read_csv("iris_with_header.csv")

df = df.drop(['petal_length', 'petal_width', 'species_type'], axis=1)

print(df)