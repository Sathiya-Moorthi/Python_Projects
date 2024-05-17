n=int(input(""))
k=[]
for i in range(n):
    m=input("")
    k.append(m)
for x in range(n):
    b=k[x]
    if b == b[::-1]:
        print(b)

