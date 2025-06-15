"""

The below code will perform the element-wise multiplication between regions and weights
 and return the sum of their results

 error find out via chatgpt
 convo link : https://chat.openai.com/share/71e8ee29-e936-4a55-9651-f0295a7a44b0

 """

import numpy as np
import math as m
from runtime import runtime

regions = np.array([73, 74, 75])
weights = np.array([2.3, 2.4, 2.6])

# The shape attribute is useful for understanding the dimensions of an array,
# especially when dealing with multidimensional arrays or when performing operations that depend on the array's shape
print("Dimension of the array:", weights.shape)
print("Dimension of the array:", np.shape(regions))

# to check the data type of numpy variables
print("Datatype of numpy variable is :", regions.dtype)

# the np.dot() function is used for matrix multiplication or dot product operation.
# Its behavior depends on the dimensions of the input arrays:

print("Final result is :", np.dot(regions, weights))

# to understand the floor and ceil function
print("Final result is :", m.ceil(np.dot(regions, weights)))

print("Final result is :", m.floor(np.dot(regions, weights)))

"""
Certainly! Let's break down the code:

1) import numpy as np: This line imports the NumPy library and assigns it the alias np. NumPy is a Python library 
used for numerical computing, especially for handling arrays and matrices.

2) regions = np.array([73, 74, 75]): This line creates a NumPy array named regions containing the values [73, 74, 75]. 
The np.array() function is used to create a NumPy array from a Python list, which is denoted by the square brackets []. 
This array represents different regions, perhaps in a geographical context.

3) weights = np.array([2.3, 2.4, 2.5]): This line creates another NumPy array named weights containing the values [2.3, 2.4, 2.5].
 Similar to the regions array, this array represents weights associated with each region.
 
4) print(np.dot(regions, weights)): This line calculates the dot product of the regions array and the weights array using NumPy's np.dot() function.
 The dot product of two arrays is a scalar value calculated by multiplying corresponding elements of the arrays and then summing up the results. 
 In this case, it's like finding the weighted sum of the regions, where the weights are given by the weights array. 
 The result will be printed to the console.


So, the output of the code will be the dot product of the regions and weights arrays, 
which represents some kind of weighted sum or aggregate value based on the regions and their associated weights.


"""

climate_data = ([[73, 54, 75],
                 [45, 46, 78],
                 [89, 78, 90],
                 [22, 33, 44]])

# The shape attribute is useful for understanding the dimensions of an array
print("Dimension of the array is :", np.shape(climate_data))

# The np.matmul() function in NumPy is used to perform matrix multiplication between two arrays.
# It differs from the * operator (np.dot() for 1D arrays) in how it handles multiplication of higher-dimensional arrays
print("Matrix multiplication of this array via matmul function is:", np.matmul(climate_data, weights))
print("Matrix multiplication of this array via dot function is :", np.dot(climate_data, weights))
print("Matrix multiplication of this array via dot function is :", climate_data @ weights)

# url.urlretrieve("need to give online url link here")

''' The np.genfromtxt() function in NumPy is used to load data from a text file, with the ability to handle missing values,
different delimiters, and other data types. 
 It returns a NumPy array containing the data read from the text file. '''

# data = np.genfromtxt('sample-1.txt', delimiter=',', skip_header=1)
# print(data)

# The above code will read data from the file named 'data.txt', assuming it's comma-separated, and skip the first row.
# Then, it will print the resulting NumPy array containing the data.

''' detail info of genformtxt will find in this link 
    convo link : https://chat.openai.com/share/71e8ee29-e936-4a55-9651-f0295a7a44b0
'''

yield1 = np.array([[22, 33, 44],
                   [33, 44, 55],
                   [44, 55, 66],
                   [55, 66, 77]])

print("Dimension of the array is :", np.shape(yield1))
# climate_result = np.concatenate((climate_data, yield1), axis=1)

# Selecting only the first column of yield1
yield1_first_cloumn = yield1[:, 0]  # Selecting only the first column of yield1

print("After selecting 1st cloumn in yiedl1 : ", yield1_first_cloumn)
print("After reshaping the yield1_first_cloumn : ", yield1_first_cloumn.reshape(-1, 1))

# Merging the first column of yield1 with climate_data
climate_result = np.concatenate((climate_data, yield1_first_cloumn.reshape(-1, 1)), axis=1)
print("After merging the yield1 data into climate_data :", climate_result)

'''
In this code:

1) yield1[:, 0] selects all rows from the first column of yield1.
2) reshape(-1, 1) reshapes the selected column to have a single column and an appropriate number of rows to match the number of rows in climate_data.
3) Finally, np.concatenate() is used to concatenate climate_data and the reshaped first column of yield1 along the columns (axis=1).

'''

np.savetxt("Climate_result.txt", climate_result,
           fmt='%.2f',
           delimiter=', ',
           header='Temperature,Rainfall,Humidity,Yield',
           comments='Storing the data of the climate_result in this file : \n\n'
           )

'''
 Let's break down each part of the np.savetxt() function call:

1) np.savetxt(): This is a function from the NumPy library used to save data to a text file.

2) "Climate_result.txt": This is the name of the file where the data will be saved. In this case, the data will be saved 
to a file named "Climate_result.txt" in the current directory.

3) climate_result: This is the data that will be saved to the file. It's assumed to be a NumPy array.

4) fmt='%.2f': This specifies the format string to use when writing the data to the file. In this case, it specifies that
 floating-point numbers should be formatted with two decimal places.
 
5) delimiter=',': This specifies the character that will be used to separate the values in the output file. 
In this case, a comma (,) is used as the delimiter.

6) header='Temperature,Rainfall,Humidity,Yield': This specifies the header that will be written at the beginning of the file.
 The header typically contains names for each column of data.
 
7) comments='': This specifies the character that will be used to indicate comments in the file. In this case, an empty 
string means that there will be no comments in the file.

Putting it all together, the np.savetxt() function call saves the data contained in the climate_result array to a 
text file named "Climate_result.txt", with each value formatted with two decimal places, separated by commas, and with a 
header row specifying the names of each column. 

There are no comments in the file.
'''
# Array and slicing in numpy arrays:

data = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],

                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(type(data))  # to find the data type of data
print("Dimension of the array is :", data.shape)
print("Indexing the data : ", data[1, 2, 2])

# others ways of creating numpy array
# Randomly create an array
print("creating an array randomly using rand function:\n ", np.random.rand(2, 3))  # random vector
print("creating an array randomly using randn function:\n ", np.random.randn(2, 3))  # random matrix

print("\n", np.linspace(3, 27, 9))  # Equally spaced numbers in a range
print("\n", np.full([2, 3], 42))  # fixed value
print("\n", np.zeros((3, 2)))  # all zeros
print("\n", np.ones((3, 2)))  # all ones
print("\n", np.eye(3))  # identity matrix
print("\n", np.arange(10, 90, 3))  # range start with start, end and step
print("\n", np.arange(10, 90, 3).reshape(3, 3, 3))  # range start with start, end and step and reshaped according to the
# specified dimensions.

# this will calculate the run time of the program, the program was already written and save as .py file in same folder
# once, that is done, just we can import to any program like " from runtime import runtime "

runtime() # and we can call that function like this

"""------------------------------------to learn more function reg Numpy check in google or chatgpt------------------------------------------"""

# the below link contains all the errors that I have faced while running this program and other convo reg numpy, must visit to learn more

"""------------------------------------ chatgpt : https://chatgpt.com/share/71e8ee29-e936-4a55-9651-f0295a7a44b0 -------------------------------------"""

