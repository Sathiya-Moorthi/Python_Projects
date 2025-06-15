import os
from os import path  # os.path.exists("Climate_result.txt")

if path.exists("Climate_result.txt"):
    print("File exists\n")
else:
    print("File not exists\n")

print(os.getcwd())  # to check the present/ current working directory
print(os.listdir())  # to get the list of the files in a directory
print(os.listdir('.'))  # relative path
print(os.listdir('/Users'))  # absolute path

if os.listdir() == os.listdir('.'):
    print('true')
else:
    print('false')

# os.mkdir('Data')
if path.exists('Data'):
    os.rmdir('Data')
    print("Directory found and deleted successfully")
else:
    print("No Directory found")

