'''
f = open(r"D:\textfile.txt", "w+")
f.write("hello")
f.close()
f = open(r"D:\textfile.txt", "r")
if f.mode == 'r':
    print(f.read())
    '''

with open(r"D:\textfile.txt", 'w+') as file:
    print(file.write("New file created successfully"))
with open(r"D:\textfile.txt", 'r+') as read_file:
    print(read_file.read())

