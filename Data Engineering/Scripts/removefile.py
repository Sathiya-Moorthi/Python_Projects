f = open("textfile.txt", "w+")
f.write("hello")
f.close()
f = open("textfile.txt", "r")
if f.mode == 'r':
    print(f.read())
