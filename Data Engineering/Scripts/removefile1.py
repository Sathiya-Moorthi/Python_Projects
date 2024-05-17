import os


def removefile():
    if os.path.exists("textfile.txt"):
        os.remove("textfile.txt")
    else:
        print("file cannot be found")


removefile()
