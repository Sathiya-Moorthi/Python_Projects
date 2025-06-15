import os
from os import path
# from os import remove as delete_file


def removefile():
    if path.exists(r"D:\textfile.txt"):
        os.remove(r"D:\textfile.txt")
        # delete_file(r"D:\textfile.txt")
        print("File found and deleted successfully")
    else:
        print("file cannot be found")


removefile()
