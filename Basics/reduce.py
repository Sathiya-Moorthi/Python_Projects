import functools
a=[1,2,3,4]
s=functools.reduce(lambda x,y:x+y,a)
print(s)