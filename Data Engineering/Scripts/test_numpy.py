import os

import numpy as np
import math as m
from runtime import runtime
from os import path

regions = np.array([73, 74, 75])
weights = np.array([2.3, 2.4, 2.6])

# print("Dimension of the array:", weights.shape)
# print("Dimension of the array:", np.shape(regions))
#
# print("Datatype:", regions.dtype)
# print("Final result is :", np.dot(regions, weights))
#
# print("Final result is :", m.ceil(np.dot(regions, weights)))
# print("Final result is :", m.floor(np.dot(regions, weights)))

climate_data = np.array([[73, 54, 75],
                         [45, 46, 78],
                         [89, 78, 90],
                         [22, 33, 44]])

# print(np.shape(climate_data))
# print("Matrix multiplication of this array via matmul function is:", np.matmul(climate_data, weights))
# print("Matrix multiplication of this array via dot function is :", np.dot(climate_data, weights))
# print("Matrix multiplication of this array via dot function is :", climate_data @ weights)

# print(climate_data.shape)
climate_first_column = climate_data[1:2]
# print(climate_data[1:2])
# print(climate_data.reshape(-3,3))

yield1 = np.array([[22, 33, 44],
                   [33, 44, 55],
                   [44, 55, 66],
                   [55, 66, 77]])

yield1_first_column = yield1[0:1]

climate_yield_data = np.concatenate((climate_data.reshape(-3, 3), yield1.reshape(-3, 3)), axis=1)
# print(climate_yield_data)
# np.savetxt(r"D:\climate_result.txt", climate_yield_data,
#            fmt='%.2f',
#            delimiter=',',
#            header='Temperature,Rainfall,Humidity,Yield'
#            )

# with open(r"D:\climate_result.txt", 'r+') as file:
#     if path.exists(r"D:\climate_result.txt"):
#         # lines = file.readline()
#         # new_line = [line.replace('#',"") for line in lines]
#         print(f"File founded:\n{file.read()}")
#     else:
#         print("No file found in this directory")

# os.remove(r"D:\climate_result.txt")

# print(type(yield1))

data = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],

                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

# print(data.dtype)  # to find the data type of data
# print("Dimension of the array is :", data.shape)
# print("Indexing the data : ", data[0, 0, 2])

# print("creating an array randomly using rand function:\n ", np.random.rand(2, 3))  # random vector
# print("creating an array randomly using randn function:\n ", np.random.randn(2, 3))

# print("\n", np.linspace(3, 27, 9))  # Equally spaced numbers in a range
# print("\n", np.full([2, 3], 42))  # fixed value
# print("\n", np.zeros((3, 2)))  # all zeros
# print("\n", np.ones((3, 2)))  # all ones
# print("\n", np.eye(4))  # identity matrix
# print("\n", np.arange(10, 90, 3))  # range start with start, end and step
# print("\n", np.arange(10, 90, 3).reshape(3, 3, 3))  # range start with start, end and step and reshaped according to the
# # # specified dimensions.