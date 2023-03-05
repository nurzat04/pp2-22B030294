def file_lengthy(fp):
    list1 = []
    with open(fp) as f:
        for i, l in enumerate(f):
            list1.append(i)
    return list1[-1] + 1
        
print(file_lengthy("C:/tsis6/text1.txt"))