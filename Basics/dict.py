def Convert(l):
    r = {l[i]: l[i + 1] for i in range(0, len(l),2)}
    return r

l = ['a', 1, 'b', 2, 'c', 3]
print(Convert(l))