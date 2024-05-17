def check_palindrome(string):
   if string==string[::-1]:
      print(string)
k=[]
n=int(input(""))
for i in range(n):
    string = input("")
    k.append(string)
for x in range(n):
    b=k[x]
    check_palindrome(b)
