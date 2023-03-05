def cal(s):
    d = {"upper case":0,"lower case":0}
    for x in s:
        if x.isupper():
            d["upper case"] += 1
        elif x.islower():
            d["lower case"] += 1
        else:
            pass
    print(d["upper case"])
    print(d["lower case"])
s = str(input())
cal(s)