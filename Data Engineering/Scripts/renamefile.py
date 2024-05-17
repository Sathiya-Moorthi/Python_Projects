import os

# os.rename("textfile.txt", "myfile.txt")

with open("sample1.txt", mode='w+') as file:
    print(file.write("add"))
    print(file.read())

