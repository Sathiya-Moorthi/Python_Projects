import re
str="This is a python"
x=re.compile('.*is')
y=x.findall(str)
print(y)