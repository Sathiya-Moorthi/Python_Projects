from os import path
import os

filepath = r"D:\new_file.txt"

with open(filepath, "w") as file:
    file.write("Hi")

with open(filepath,"r") as file:
    print(file.read())

if path.exists(filepath):
    os.remove(filepath)
    print("removed successfully")
else:
    print("no file presents")