try:
    a=10;b=0
    c=a/b
except Exception as e:  # except: print("Division by zero error")
    print(e)
else:
    print("error occured")