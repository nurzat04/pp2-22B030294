alpha = ['a', 'b', 'c', 'd', 'e']
with open("C:/tsis6/text1.txt", "w") as f:
    for i in alpha:
        f.write("%s\n" % i)
fp = open("C:/tsis6/text1.txt")
print(fp.read())
