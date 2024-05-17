def prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                c.append(num)
                break
        else:
            d.append(num)
n=int(input(""))
k=[]
c=[]
d=[]
e=[]
for i in range(n):
    a=int(input(""))
    k.append(a)
for j in range(n):
    b=k[j]
    prime(b)
e.append(d)
print("0")
e.append(c)
print(e)