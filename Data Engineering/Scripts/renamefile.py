import os
from os import path

# os.rename(r"D:\textfile.txt", r"D:\myfile.txt")

with open(r"D:\textfile.txt", mode='w+') as file:
    print(file.write("add"))
    print(file.read())


def remove_file():
    file_path = r"D:\textfile.txt"
    if path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} found and deleted successfully")
    else:
        print(f"No file found", file_path)


remove_file()
