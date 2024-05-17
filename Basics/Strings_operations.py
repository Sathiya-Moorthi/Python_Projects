n = int(input())
string = []
for i in range(n):
    string += list(map(str, input().split(" ")))


# set1 = list(OrderedSet(string))
def unique(string):
    string1 = []
    if len(string) == 3:
        for i in string:
            for j in i:
                if j not in string1:
                    string1 += j
        return "".join(map(str, string1))
    elif len(string) == 2:
        for i in string:
            string2 = ""
            for j in i:
                if j not in string2:
                    string2 += j
            string1 += string2
        return "".join(map(str, string1))


print(unique(string))

# print("".join(map(str,set1)))
