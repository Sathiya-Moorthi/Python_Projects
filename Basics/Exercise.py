# 7 #
'''
seq = ['soup', 'dog', 'cat', 'salad', 'great']
out = list(filter(lambda same: same[0] == "s", seq))
print(out)

'''

# 8 #

'''

def find_speed(kilo):
    if kilo <= 60:
        return "No Result"
    elif (kilo > 61) and (kilo < 81):
        return "Small Ticket"
    elif kilo >= 81:
        return "Big Ticket"

speed = int(input("enter the kilometer of the speed: "))
x = find_speed(speed)
print(x)

'''


# 3 #

'''
planet = "earth"
diameter = 12742

print("the diameter if the {} is {} ".format(planet,diameter))

'''

# 5 #

'''

def gmail(g_mail):
    k = mail.split('@')
    return k

mail = "user@domian.com"
x = gmail(mail)
print(x[1])

'''

# 6 #

'''

def find_dog(inp):
    for i in inp:
        if "dog" in inp:
            return "True"
        else:
            return "False"

input_string = "Is there is any dog there ?"
x = find_dog(input_string.lower())
print(x)

'''

# 7 #

'''

c = 1
def count_of_max(inp):
    for i in inp:
        if "dog" in inp:
            return c+1

count_dog = "This dog runs faster than other dogs dude !"

x = count_of_max(count_dog)
print(x)

'''

s=[]
for i in range(3):
    string = input("Enter the string :")
    s.append(string.capitalize())  # it will capitalize only the 1st letter of the string
print(s)



