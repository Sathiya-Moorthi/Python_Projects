def vowels(string):
    vow=set('aeiou')
    for j in string:
        if j in vow:
           break
    else:
        print(string)

n=int(input(""))
k=[]
for i in range(n):
    str=input("")
    k.append(str)
print("Strings without vowels:")
for x in range(n):
    b=k[x]
    vowels(b)
