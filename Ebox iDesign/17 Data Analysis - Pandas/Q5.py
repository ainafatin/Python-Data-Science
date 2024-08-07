# Rename Column in Data Frame

# Write a Python program to rename a specific column in a Data Frame.

# Import the given CSV file as a Data Frame.

# Print the column names using columns attribute.

# Rename the column “species_type” to “SpeciesType”

# Print the column names using columns attribute.

# Print the entire contents of the Data Frame

# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

# The input file is given as part of the template code.

import pandas as pd

df = pd.read_csv("iris_with_header.csv")

print("Column Names")
print(df.columns)

df.rename(columns={"species_type":"Species Type"}, inplace=True)

print("Column Names after renaming")
print(df.columns)

print("DataFrame")
print(df)