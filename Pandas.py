"""
author: Alejandro Guevara
"""
import pandas as pd
import numpy as np

df = pd.read_csv('salaries.csv') # Create a DataFrame from a CSV file
print(df)

print(df['Name']) # Accessing data using its column name

print(df[['Name', 'Salary']]) # Accessing more than one column, using a list
                               # of names

ageMean = df['Age'].mean() # Computes average on the data in the 'Age' column
print("Age average is: "+ str(ageMean))

print(df['Age'] > 30 ) # Applies the comparator to every element in the column
                       # and returns the boolean results

age_filter = df['Age'] > 30 # It can be saved and used as a filter
print(df[age_filter])

data = np.random.randint(0, 100, (10, 5))
df = pd.DataFrame(data, columns=list('ABCDE')) # Create a DataFrame from a numpy
print(df)                                      # array, letting Pandas create a
                                               # default index.

print(df.head()) # Returns the first 5 rows of the Dataframe
print(df.tail()) # Returns the last 5 rows of the Dataframe

dates = pd.date_range('20180221', periods=10) # Returns an index made of datetime
df = pd.DataFrame(data, columns=list('ABCDE'), index=dates)
print(df)                           # Create a DataFrame from a numpy
                                    # array, using DateTime as index

print(df.describe()) # Returns valuable statistical info about the data
print(df.describe().T) # Transposes a Dataframe

print(df.sort_values(by='B')) # Sorts the DataFrame by the values in one of the
                              # columns

print(df[0:3]) # Dataframes accept slicing
print(df['20180225':'20180228']) # it is also a valid way to slice a dataframe

df.plot(x='A', y='B', kind='scatter') # DataFrames can be plotted
