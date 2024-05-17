import pandas as pd
import matplotlib.pyplot as plt
from runtime import runtime

''' --------------------------------1. Reading a CSV file using Pandas--------------------------------------'''

file_path = r"D:\Gayu's Project\titanic_dataset.csv"

titanic_data_df = pd.read_csv(file_path)  # Here, df indicates dataframe

print(titanic_data_df)  # Reading the datas from the CSV file using pandas
print(titanic_data_df.info())  # Getting the info about the titanic_data
print(titanic_data_df.describe())  # Getting the statistical info about the titanic_data

# To get the info about the columns present in the titanic_data
print("Info about the columns present in the titanic_data : \n", titanic_data_df.columns, "\n")

# To get the number of rows and columns as tuple present in the file
print("Rows : {} \nColumns : {} \n".format(titanic_data_df.shape[0], (titanic_data_df.shape[1])))
print(titanic_data_df.shape)  # To get the number of rows and columns as tuple

''' --------------------------------2. Retrieving data from a data frame-------------------------------------- '''

print(titanic_data_df["Sex"])  # retrieving the columns as series using column name
print(titanic_data_df["Sex"][890])  # retrieving both columns values from a series using index
print(titanic_data_df.at[890, "Sex"])  # retrieving single value from the data frame

# Each column is represented using a data structure called `Series`,
# which is essentially a numpy array with some extra methods and properties.
print(type(titanic_data_df["Sex"]))

titanic_data_df_copy = titanic_data_df.copy()  # to create a deep copy of a data frame
if titanic_data_df.equals(titanic_data_df_copy):  # to compare two DataFrames
    print("DataFrames are equal\n")
else:
    print("DataFrames are not equal\n")

print(titanic_data_df.loc[890], "\n")  # retrieving a row or range of rows of data from the data frame
print(titanic_data_df.head(5), "\n")  # to print the first sequence of rows from the DataFrame
print(titanic_data_df.tail(5), "\n")  # to print the last sequence of rows from the DataFrame

# retrieving multiple rows of data from the data frame
print(titanic_data_df.sample, "\n")
print(titanic_data_df.sample(5), "\n")

#  Finding the first non-empty index in a series
print(titanic_data_df.first_valid_index, "\n")
print(titanic_data_df.Survived.first_valid_index, "\n")

''' --------------------------------3. Analyzing data from data frames--------------------------------------- '''

print("The survived passengers in the titanic ship is ", titanic_data_df.Survived.sum(), "\n")

print("The ratio of the survived passengers in the ship is {:.3f} %".format(
    titanic_data_df.Survived.sum() / titanic_data_df.PassengerId.sum()), "\n")

''' ----------------------------------4. Querying and sorting rows------------------------------------------ '''

survived_passengers = titanic_data_df.Survived > 0
print(survived_passengers)  # this will return the result in boolean of survived passengers more than zero in that
# series

print(titanic_data_df[survived_passengers])  # this will return the list of details of survived passengers more than
# zero

'----------- OR ------------'

print(titanic_data_df[titanic_data_df.Survived > 0])

'-----------------------------'

print(titanic_data_df[survived_passengers].Fare)


print(titanic_data_df_copy.drop("Embarked", axis=1, inplace=True))  # removing one or more columns from the dataframe
print(titanic_data_df_copy)

''' ------------------------------------5. Working with dates------------------------------------------ '''


# Assuming you have a DataFrame named 'df'
# Create a new column named 'date' with sequential dates starting from '2024-05-10'

start_date = '2024-05-10'
num_days = len(titanic_data_df)  # Number of rows in the DataFrame
titanic_data_df['date'] = pd.date_range(start=start_date, periods=num_days)

# Display the DataFrame with the new date column
print(titanic_data_df.date,"\n")
print(titanic_data_df.date.dtype,"\n")

titanic_data_df['year']= pd.DatetimeIndex(titanic_data_df.date).year
titanic_data_df['month']= pd.DatetimeIndex(titanic_data_df.date).month


"""
If you want to print all the columns in the DataFrame along with their values, you can use the DataFrame object itself. 
By default, pandas will truncate the display of columns if there are too many, but you can adjust this behavior using pd.set_option(). 
Here's how you can print all the columns:

"""

pd.set_option('display.max_columns',None)
print(titanic_data_df)

"""
By setting 'display.max_columns' to None, pandas will display all the columns in the DataFrame without truncating them.

Alternatively, if you just want to print the column names without displaying the entire DataFrame, you can use the .columns attribute of the DataFrame:

"""

print(titanic_data_df.columns,"\n")

'''------------------------------------6. Grouping and aggregation------------------------------------------'''

titanic_data_df= titanic_data_df.groupby('month')[['Survived','Pclass']].sum()
print(titanic_data_df)

'''------------------------------------7. Merging data from multiple sources------------------------------------------'''

# We can merge this data into our existing data frame by adding more columns.
# However, to merge two data frames, we need at least one common column

# Syntax:
''' new_dataframe_name = dataframe_that_you_want_to_merge_with.merge(dataframe_that_you_want_to_merge, on="common_column_name") '''

'''------------------------------------8. Writing data back to files------------------------------------------'''

# we can store our final result as a csv or Excel file
'''  CSV -- pd.to_csv() '''
''' Excel -- pd.to_excel '''

# Example :

''' dataframe_name_that_you_want_to_convert.to_csv('filename.csv', index=None) '''

# The to_csv function also includes an additional column for storing the index of the dataframe by default.
# We pass index=None to turn off this behavior.

''' ------------------------------------10.  Basic Plotting with Pandas------------------------------------------'''

# We generally use a library like matplotlib or seaborn plot graphs within a Jupyter notebook.
# However, Pandas dataframes & series provide a handy .plot method for quick and easy plotting.

''' titanic_data_df.Survived.plot(); '''

# the above line will plot the graph inform of visual representation but this is not working in PyCharm without matplotlib, working in Jupyter notebook.


"""------------------------------------to learn more function reg Pandas check in google or chatgpt------------------------------------------"""

# the below link contains all the errors that I have faced while running this program and other convo reg pandas, must visit to learn more

"""------------------------------------ chatgpt : https://chatgpt.com/share/666174cd-2f8c-4cff-8eac-ac6eed87dfe6 ------------------------------------------ """


