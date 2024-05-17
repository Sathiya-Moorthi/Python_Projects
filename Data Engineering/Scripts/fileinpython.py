def main():
    f = open("Climate_result.txt", "r")
    print(f.read())
    f = open("Climate_result.txt", "a")
    print(f.write('add'))

'''
    for i in range(10):
        f.write(" appended line %d\n" % (i))
    f.close()
    f = open("textfile.txt", "r")
    if f.mode == 'r':
        print(f.read()) 
        
        '''
        


main()
